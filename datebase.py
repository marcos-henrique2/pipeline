import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

# Carregar  variaveis do arquivo .env
load_dotenv()

# Configuraçao do banco de dados PostgreSQL
DB_HOTS = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Funçao para salvar os dados validados no postgresSQL


def salvar_no_postegres(dados: Vendas):
    try:
        conn = psycopg2.connect(
            host=DB_HOTS,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()

        # Inserçao dos dados na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO vendas(email, data, valor, quantidade, produto) VALUES(%s, %s,  %s, %s, %s)"

        )
        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")
