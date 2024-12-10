import streamlit as st
import requests
from dotenv import load_dotenv
import os
import json

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter valores das variáveis de ambiente
API_URL = os.getenv("LANGFLOW_API_URL")
API_TOKEN = os.getenv("LANGFLOW_API_TOKEN")
API_DATA = os.getenv("LANGFLOW_API_DATA")

# Verificar se as variáveis de ambiente foram configuradas corretamente
if not API_URL or not API_TOKEN or not API_DATA:
    st.error("Variáveis de ambiente LANGFLOW_API_URL, LANGFLOW_API_TOKEN e LANGFLOW_API_DATA não configuradas.")
    st.stop()

# Converter API_DATA de string para dicionário
try:
    API_DATA = json.loads(API_DATA)
except json.JSONDecodeError:
    st.error("O formato do JSON em LANGFLOW_API_DATA é inválido.")
    st.stop()

st.title("📄 Smart Doc Assistant")

"""
Olá! Eu sou o Smart Doc Assistant, seu assistente inteligente para consultas e resumos de documentos. 
Envie suas perguntas e eu ajudo a encontrar as respostas nos documentos com rapidez e precisão.
"""

# Inicializar o estado da sessão para armazenar o histórico de conversas
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Olá! Como posso ajudar com seus documentos hoje?"}]

# Exibir mensagens de chat do histórico da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Aceitar entrada do usuário
if prompt := st.chat_input("Digite uma mensagem para o assistente:"):
    # Adicionar a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Enviar solicitação para a API do Langflow
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_TOKEN}"
        }
        # Atualizar o valor do input no JSON carregado
        API_DATA["input_value"] = prompt

        response = requests.post(API_URL, headers=headers, json=API_DATA)
        response_data = response.json()

        # Extrair a resposta do assistente
        assistant_message = response_data["outputs"][0]["outputs"][0]["results"]["message"]["text"]

        # Exibir mensagem do assistente no chat
        with st.chat_message("assistant"):
            st.markdown(assistant_message)

        # Adicionar mensagem do assistente ao histórico de conversas
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

    except Exception as e:
        st.error(f"Erro ao consultar a API: {e}")
