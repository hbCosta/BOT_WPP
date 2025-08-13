import os 
import requests

# Carrega as variáveis de ambiente do arquivo .env
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_INSTANCE_TOKEN = os.getenv("ZAPI_INSTANCE_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

# URL DA API
ZAPI_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_INSTANCE_TOKEN}/send-text"

def send_message(contact_phone, contact_name):
    message = f"Olá {contact_name}, tudo bem com você?"

    # monta o headers e o payload
    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_CLIENT_TOKEN
    }
    payload = {
        "phone": contact_phone,
        "message": message
    }
    try:
        # Faz a requisição POST para enviar a mensagem
        response = requests.post(ZAPI_URL, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"Mensagem enviada para {contact_name} ({contact_phone})")
        else:
            print(f"Falha ao enviar mensagem para {contact_name} ({contact_phone}): {response.text}")
    except Exception as e: # Trata os erros 
        print(f"Erro de conexão: {e}")
