# --- Meu Diário de Bordo (database.py) ---

# Aqui eu importo as ferramentas do SQLAlchemy que vou precisar.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Configuração do Banco de Dados

# Essa é a 'connection string', o "endereço" do meu banco.
# Como estou usando SQLite, meu banco de dados será apenas um arquivo
# chamado 'livraria.db' na mesma pasta do projeto.
DATABASE_URL = "sqlite:///./livraria.db"

# 'create_engine' é o ponto de entrada principal para o SQLAlchemy.
# É ele que "sabe" como se conectar ao banco de dados (neste caso, o arquivo SQLite).
# O argumento 'connect_args' é específico para o SQLite,
# ele permite que mais de uma "thread" converse com o banco.
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# 2. Configuração da "Sessão"

# 'SessionLocal' é uma "fábrica de sessões" (conexões) com o banco.
# Cada vez que eu precisar fazer uma operação no banco (criar, ler, atualizar, deletar),
# eu vou pedir uma nova sessão para essa fábrica.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. A Base dos Modelos

# 'Base' é uma classe "mágica" do SQLAlchemy.
# Todos os meus modelos de tabela (como o futuro modelo 'Livro')
# vão ter que herdar dela para que o SQLAlchemy saiba
# como "traduzir" minha classe Python para uma tabela no banco.
Base = declarative_base()