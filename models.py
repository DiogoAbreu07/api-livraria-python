# --- Meu Diário de Bordo (models.py - Versão 2.0 CORRIGIDA) ---

# A importação deve incluir 'Boolean' agora, para o Usuario.
from sqlalchemy import Column, Integer, String, Boolean

# Importação da Base
from database import Base

# --- MODELO DE LIVRO (Definição ÚNICA) ---
# Aqui está sua classe Livro, definida APENAS UMA VEZ.
class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor = Column(String, index=True)
    ano_publicacao = Column(Integer)

# --- MODELO DE USUÁRIO (A nova classe) ---
# E aqui está a nova classe Usuario, logo abaixo.
class Usuario(Base):
    __tablename__ = "usuarios"

    # 'id': A chave primária.
    id = Column(Integer, primary_key=True, index=True)

    # 'email': Será o "login". Tem que ser único (unique=True).
    email = Column(String, unique=True, index=True, nullable=False)

    # 'hashed_password': A senha CRIPTOGRAFADA. Nunca salvar senha em texto!
    hashed_password = Column(String, nullable=False)

    # 'is_active': Útil para "desativar" um usuário sem apagá-lo.
    is_active = Column(Boolean, default=True)