# --- Meu Diário de Bordo (main.py - Versão 5.0 PROJETO 2 FINAL) ---

# --- Importações ---
from fastapi import FastAPI, Depends, HTTPException, status # <-- NOVO: importei 'status'
from sqlalchemy.orm import Session
from typing import List
import schemas
import models
import auth # Importamos nosso arquivo de autenticação
from database import engine, SessionLocal
# --- NOVO: Importa o esquema de segurança e o de dados do token ---
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# --- Criação das Tabelas ---
models.Base.metadata.create_all(bind=engine)

# --- Instância do FastAPI ---
app = FastAPI(
    title="API de Livraria Pessoal",
    description="Uma API RESTful para gerenciar uma coleção pessoal de livros.",
    version="0.1.0"
)

# --- Dependência de Banco de Dados ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------------------------
# === O "SEGURANÇA" (Nova Dependência) ===
# -----------------------------------------------

# --- NOVO: Define o "esquema" de autenticação ---
# Isso diz ao FastAPI: "Eu vou usar autenticação do tipo Bearer Token,
# e o endpoint que gera o token fica na URL '/login'".
# Ele vai procurar por um header "Authorization: Bearer <token>"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# --- NOVO: A Dependência "get_current_user" ---
# Esta é a função "segurança de boate".
# Qualquer endpoint que "depender" dela, vai rodar este código primeiro.
def get_current_user(
    token: str = Depends(oauth2_scheme), # 1. Exige o token (vem do header)
    db: Session = Depends(get_db)        # 2. Pega a sessão do banco
) -> models.Usuario:
    
    # 3. Prepara o erro que vamos usar se o token for inválido
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # 4. Tenta verificar o token usando nossa função do auth.py
    payload = auth.verify_token(token, credentials_exception)
    
    # 5. Pega o email (que guardamos no 'sub') de dentro do token
    email: str = payload.get("sub")
    if email is None:
        raise credentials_exception
        
    # 6. Busca o usuário no banco de dados
    user = db.query(models.Usuario).filter(models.Usuario.email == email).first()
    if user is None:
        # Se o email do token não existir mais no banco
        raise credentials_exception
        
    # 7. Se tudo deu certo, retorna o objeto 'user'
    return user


# -----------------------------------------------
# === ENDPOINTS DE AUTENTICAÇÃO E USUÁRIOS ===
# (Sem mudanças aqui)
# -----------------------------------------------

@app.post("/usuarios", response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")
    
    hashed_password = auth.get_password_hash(usuario.password)
    db_usuario = models.Usuario(email=usuario.email, hashed_password=hashed_password)
    
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@app.post("/login", response_model=schemas.Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(models.Usuario).filter(models.Usuario.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


# -----------------------------------------------
# === ENDPOINTS DE LIVROS (AGORA PROTEGIDOS) ===
# -----------------------------------------------

# === ENDPOINT DE CRIAÇÃO (PROTEGIDO) ===
@app.post("/livros", response_model=schemas.Livro)
def create_livro(
    livro: schemas.LivroCreate,
    db: Session = Depends(get_db),
    # --- NOVO: A "TRAVA" DE SEGURANÇA ---
    # Ao adicionar esta dependência, o FastAPI *exige* que o 'get_current_user'
    # rode primeiro. Se o token for inválido, esta função nem é executada.
    current_user: models.Usuario = Depends(get_current_user)
):
    # (Note: não estamos *usando* o 'current_user' aqui,
    # mas o simples fato de pedi-lo, protege o endpoint.)
    db_livro = models.Livro(**livro.model_dump())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro

# === ENDPOINT DE LEITURA (PÚBLICO) ===
# Não vamos proteger os GETs. É comum que a leitura seja pública.
@app.get("/livros/{livro_id}", response_model=schemas.Livro)
def read_livro(livro_id: int, db: Session = Depends(get_db)):
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return db_livro

# === ENDPOINT DE LEITURA (PÚBLICO) ===
@app.get("/livros", response_model=List[schemas.Livro])
def read_livros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    livros = db.query(models.Livro).offset(skip).limit(limit).all()
    return livros

# === ENDPOINT DE ATUALIZAÇÃO (PROTEGIDO) ===
@app.put("/livros/{livro_id}", response_model=schemas.Livro)
def update_livro(
    livro_id: int,
    livro: schemas.LivroCreate,
    db: Session = Depends(get_db),
    # --- NOVO: A "TRAVA" DE SEGURANÇA ---
    current_user: models.Usuario = Depends(get_current_user)
):
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    db_livro.titulo = livro.titulo
    db_livro.autor = livro.autor
    db_livro.ano_publicacao = livro.ano_publicacao

    db.commit()
    db.refresh(db_livro)
    return db_livro

# === ENDPOINT DE DELEÇÃO (PROTEGIDO) ===
@app.delete("/livros/{livro_id}")
def delete_livro(
    livro_id: int,
    db: Session = Depends(get_db),
    # --- NOVO: A "TRAVA" DE SEGURANÇA ---
    current_user: models.Usuario = Depends(get_current_user)
):
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    db.delete(db_livro)
    db.commit()
    return {"detail": f"Livro com id {livro_id} foi deletado com sucesso."}