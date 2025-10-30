# --- Meu Diário de Bordo (schemas.py) ---

# 'BaseModel' é a classe principal do Pydantic.
# Meus "contratos" (schemas) vão herdar dela.
from pydantic import BaseModel

# Este é o "contrato" base.
# Ele tem os campos que são comuns tanto na criação quanto na leitura.
class LivroBase(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int

# Este é o "contrato" de CRIAÇÃO (Create).
# Quando alguém for enviar um livro novo para minha API (POST),
# o JSON deve ter exatamente estes campos.
# Por enquanto, ele é idêntico ao Base.
class LivroCreate(LivroBase):
    pass  # 'pass' significa que ele não tem campos extras.

# Este é o "contrato" de LEITURA (Read).
# Quando minha API DEVOLVER um livro, ela vai usar este formato.
# Note que ele tem o 'id', que o banco de dados gera sozinho.
class Livro(LivroBase):
    id: int

    # Esta configuração 'from_attributes = True' (antes era 'orm_mode')
    # é uma mágica do Pydantic. Ela diz: "Você pode ler os dados
    # diretamente de um objeto SQLAlchemy (meu 'models.Livro')
    # e não só de um dicionário."
    # Isso faz a "tradução" do 'models.Livro' para 'schemas.Livro'
    # ser automática.
    class Config:
        from_attributes = True