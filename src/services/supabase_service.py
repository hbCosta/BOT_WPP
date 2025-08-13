import os
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
TABLE_NAME = os.getenv("TABLE_NAME")   

# Verifica se as variáveis de ambiente estão definidas
if not SUPABASE_URL or not SUPABASE_KEY or not TABLE_NAME:
    raise ValueError("As variáveis de ambiente devem estar definidas.")

# Cria cliente para interagir com o banco de dados
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def search_contacts():
    # Tenta buscar os registros da tabela
    try:
        response = supabase.table(TABLE_NAME).select("*").execute()
        return response.data
    # Se ocorrer um erro, imprime a mensagem de erro
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return None
