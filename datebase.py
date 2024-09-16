import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

# Carregar  variaveis do arquivo .env
load_dotenv()

#Configuraçao do banco de dados PostgreSQL
DB_HOTS = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")