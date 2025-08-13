import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis de ambiente do arquivo .env

from services.supabase_service import search_contacts
from services.zapi_service import send_message


def main():
    # Busca os contatos do banco de dados
    contacts = search_contacts()
    
    # Se algum contato for encontrado  envia mensagem para cada um
    if contacts:
        print("Contatos encontrados:", contacts)
        for contact in contacts:
            send_message(contact['Phone'], contact['Name'])
    else:   # Se nenhum contato for encontrado, informa ao usuário
        print("Nenhum contato encontrado.")

if __name__ == "__main__":
    main()

