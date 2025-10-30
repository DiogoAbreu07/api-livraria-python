# --- Meu Diário de Bordo (auth.py) ---

# Vou importar as bibliotecas de segurança que instalamos.
from passlib.context import CryptContext  # Para hashear senhas
from jose import JWTError, jwt           # Para criar e verificar Tokens JWT
from datetime import datetime, timedelta, timezone # Para definir o tempo de expiração do token

# --- Configuração de Segurança ---

# 1. Configuração do Hash de Senha (usando bcrypt)
# Esta é a "fórmula" que o passlib vai usar para criptografar.
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# 2. Configuração do Token JWT (o "Crachá")
# Esta é a "chave secreta" que o JWT usa para assinar os tokens.
# **IMPORTANTE:** No mundo real, isso NUNCA deve estar no código.
# Deve vir de uma variável de ambiente (falaremos disso no Projeto 3).
SECRET_KEY = "sua_chave_secreta_muito_dificil_de_adivinhar"
ALGORITHM = "HS256"  # O algoritmo de assinatura.
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # O "crachá" expira em 30 minutos.

# --- Funções de Segurança ---

# Função 1: Verificar se a senha pura bate com a senha hasheada
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compara a senha em texto puro (enviada no login) com
    a senha criptografada (salva no banco).
    """
    return pwd_context.verify(plain_password, hashed_password)

# Função 2: Criar o hash da senha
def get_password_hash(password: str) -> str:
    """
    Recebe uma senha em texto puro e retorna
    o "hash" (versão criptografada) dela.
    """
    return pwd_context.hash(password)

# Função 3: Criar o Token JWT
def create_access_token(data: dict) -> str:
    """
    Cria o "crachá" (Token JWT) baseado nos dados do usuário.
    """
    # 1. Pega os dados que eu quero guardar dentro do token
    to_encode = data.copy()

    # 2. Define o tempo de expiração
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # 3. Adiciona a expiração ("exp") ao dicionário
    to_encode.update({"exp": expire})

    # 4. "Assina" o token com minha chave secreta e algoritmo
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

# Função 4: Verificar e Decodificar o Token JWT (será usada depois)
def verify_token(token: str, credentials_exception) -> dict:
    """
    Verifica se o token é válido e o decodifica,
    retornando os dados (payload) que estão dentro dele.
    """
    try:
        # Tenta decodificar o token usando a mesma chave secreta
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Pega o email de dentro do token
        email: str = payload.get("sub")
        if email is None:
            # Se não tiver email, o token é inválido
            raise credentials_exception
        
        # Retorna os dados que estavam no token (o email)
        return payload
    
    except JWTError:
        # Se o 'jwt.decode' falhar (token expirado, assinatura errada),
        # ele levanta o erro.
        raise credentials_exception