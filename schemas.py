# --- Meu Diário de Bordo (schemas.py - Versão 2.2 CORRIGIDA) ---

# Vamos importar 'Field' do Pydantic
from pydantic import BaseModel, Field

# E vamos importar 'Optional' do 'typing' (AQUI ESTAVA O ERRO)
from typing import Optional

# --- SCHEMAS DE LIVRO (Existentes) ---

class LivroBase(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int

class LivroCreate(LivroBase):
    pass

class Livro(LivroBase):
    id: int

    class Config:
        from_attributes = True


# --- SCHEMAS DE USUÁRIO (Com Validação) ---

class UsuarioBase(BaseModel):
    email: str

# 'UsuarioCreate': O que eu preciso receber para CADASTRAR um usuário.
class UsuarioCreate(UsuarioBase):
    # Regras de validação para a senha
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

# 'Usuario': O que eu vou DEVOLVER quando buscar um usuário.
class Usuario(UsuarioBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

# --- SCHEMAS DE TOKEN (Novos) ---

class Token(BaseModel):
    access_token: str
    token_type: str

# 'TokenData': Os dados que eu vou guardar "dentro" do Token.
class TokenData(BaseModel):
    email: Optional[str] = None