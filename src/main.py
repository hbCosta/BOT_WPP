import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis de ambiente do arquivo .env

from services.supabase_service import search_contacts
#from services.zapi_service import send_message


def main():
    contacts = search_contacts()
    print("Contatos encontrados:", contacts)
if __name__ == "__main__":
    main()

