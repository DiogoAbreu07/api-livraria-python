# --- Meu Diário de Bordo (models.py) ---

# Vou importar as classes 'Column', 'Integer', 'String'
# para definir os tipos das minhas colunas na tabela.
from sqlalchemy import Column, Integer, String

# Também preciso importar a 'Base' que eu criei no database.py.
# É ela que vai "ligar" esta classe ao SQLAlchemy.
from database import Base

# Esta é a minha classe "Modelo" (Model).
# Ela representa a tabela 'livros' no meu banco de dados.
class Livro(Base):
    # '__tablename__' é obrigatório. É o nome real da tabela no banco.
    __tablename__ = "livros"

    # Agora eu defino as colunas da minha tabela:
    
    # 'id': Vai ser um número Inteiro, é a chave primária (primary_key=True)
    # e vai se auto-incrementar (index=True, embora o autoincrement seja implícito com pk).
    id = Column(Integer, primary_key=True, index=True)

    # 'titulo': Vai ser uma String (texto).
    titulo = Column(String, index=True)

    # 'autor': Também uma String.
    autor = Column(String, index=True)

    # 'ano_publicacao': Um Inteiro para guardar o ano.
    ano_publicacao = Column(Integer)