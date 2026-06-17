# Arquivo: database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# String de conexão:
URL_BANCO_DADOS = "mysql+pymysql://root:@localhost:3306/inova_inventario"

# O Engine é o motor que traduz o Python para o dialeto do MySQL
engine = create_engine(URL_BANCO_DADOS)

# A Sessão é o "túnel" por onde os dados vão trafegar
SessaoLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para criar as tabelas
Base = declarative_base()

# Função auxiliar para injetar a sessão nas rotas
def obter_banco():
    banco = SessaoLocal()
    try:
        yield banco
    finally:
        banco.close()