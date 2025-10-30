# --- Meu Diário de Bordo (main.py - Versão 3.0 FINAL) ---

# --- Importações ---
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas
import models
from database import engine, SessionLocal

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


# --- Endpoints da API ---

@app.get("/")
def read_root():
    return {"status": "API da Livraria no ar!"}


# === ENDPOINT DE CRIAÇÃO (CREATE) ===
@app.post("/livros", response_model=schemas.Livro)
def create_livro(
    livro: schemas.LivroCreate,
    db: Session = Depends(get_db)
):
    db_livro = models.Livro(**livro.model_dump())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro


# === ENDPOINT DE LEITURA (GET por ID) ===
@app.get("/livros/{livro_id}", response_model=schemas.Livro)
def read_livro(
    livro_id: int,
    db: Session = Depends(get_db)
):
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return db_livro


# === ENDPOINT DE LEITURA (GET Todos) ===
@app.get("/livros", response_model=List[schemas.Livro])
def read_livros(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    livros = db.query(models.Livro).offset(skip).limit(limit).all()
    return livros


# === ENDPOINT DE ATUALIZAÇÃO (UPDATE) ===

# @app.put("/livros/{livro_id}"):
#   - .put: É o método HTTP para "substituir" (Update) um recurso.
#   - "/livros/{livro_id}": A URL do recurso que queremos atualizar.
# response_model=schemas.Livro:
#   A resposta vai ser o livro já com os dados atualizados.
@app.put("/livros/{livro_id}", response_model=schemas.Livro)
def update_livro(
    livro_id: int,                  # 1. O ID do livro a ser atualizado (vem da URL).
    livro: schemas.LivroCreate,     # 2. O JSON com os *novos* dados (vem do Body).
    db: Session = Depends(get_db)   # 3. A conexão com o banco.
):
    # 4. Lógica de busca:
    #    Primeiro, preciso encontrar o livro no banco.
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()

    # 5. Tratamento de Erro 404:
    #    Se ele não existir, não tenho o que atualizar. Retorno o erro.
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    # 6. Lógica de Atualização:
    #    Se encontrou, eu atualizo *campo por campo* do objeto
    #    'db_livro' (do SQLAlchemy) com os dados que vieram
    #    no 'livro' (do Pydantic).
    db_livro.titulo = livro.titulo
    db_livro.autor = livro.autor
    db_livro.ano_publicacao = livro.ano_publicacao

    # 7. Operações no Banco:
    db.commit()       # "Commita" a atualização.
    db.refresh(db_livro)  # Refresca o objeto com os dados do banco.
    
    # 8. Retorno:
    #    Retorna o objeto 'db_livro' atualizado.
    return db_livro


# === ENDPOINT DE DELEÇÃO (DELETE) ===

# @app.delete("/livros/{livro_id}"):
#   - .delete: O método HTTP para "apagar" um recurso.
@app.delete("/livros/{livro_id}")
def delete_livro(
    livro_id: int,                  # 1. O ID do livro a ser deletado (vem da URL).
    db: Session = Depends(get_db)   # 2. A conexão com o banco.
):
    # 3. Lógica de busca:
    #    Mesma coisa, primeiro preciso encontrar o livro.
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()

    # 4. Tratamento de Erro 404:
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    # 5. Lógica de Deleção:
    db.delete(db_livro)  # "Banco, apague este objeto."
    db.commit()          # "Commita" a deleção.

    # 6. Retorno:
    #    Para o DELETE, um retorno padrão é uma mensagem de sucesso.
    #    (O 'response_model' não foi definido, então posso retornar um dict).
    return {"detail": f"Livro com id {livro_id} foi deletado com sucesso."}