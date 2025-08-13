Um guia rápido para configurar e rodar o BOT para mensagens no WhatsApp

1. Pré-Requisitos
   Tenha o Python e o pip instalados no seu computador.
2. Configuração do Supabase
   1. Crie uma tabela chamada Contatos
   2. Adicione as colunas:
      id (integer, primary key)
      Name(text)
      Phone(text)
   3. Habilite o Row Level Security (RLS)
   4. Crie uma política RLS para permitir leitura:
      Ação: SELECT
      Using: TRUE
3. Variáveis de Ambiente
   Crie um arquivo .env na raiz do projeto com:
      ```env
      SUPABASE_URL=URL_DO_SUPABASE
      SUPABASE_KEY=CHAVE_DO_SUPABASE
      TABLE_NAME=Contatos
      ZAPI_INSTANCE_ID = ID_INSTANCIA
      ZAPI_INSTANCE_TOKEN=SEU_TOKEN_ZAPI
      ZAPI_URL=URL_ZAPI_INSTANCIA
      ZAPI_CLIENT_TOKEN= TOKEN_SEGURANCA_CONTA

4. Rodar
   No terminal, execute:
      `python src/main.py`


O programa buscará contatos no Supabase e enviará mensagens via Z-API
