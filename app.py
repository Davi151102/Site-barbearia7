import streamlit as st
from datetime import datetime, date
import random
import requests # Necessário para enviar mensagens via API futuramente

# Configuração Premium
st.set_page_config(page_title="BARGEND | Sistema Inteligente", page_icon="✂️", layout="wide")

# --- DATABASE EM SESSÃO ---
if 'agenda' not in st.session_state:
    st.session_state.agenda = []
if 'estoque' not in st.session_state:
    st.session_state.estoque = {
        "Pomada Modeladora": 15, "Shampoo Ice": 10, "Óleo Premium": 5, "Creme Barba": 8
    }

# --- CONFIGURAÇÕES ---
SENHA_ADM = "ramos657"
NUMEROS_NOTIFICACAO = ["5531993276411", "5531991927401"]

UNIDADES = {
    "Unidade 1 - Bairro Ipê": {"end": "Rua Herculano Soares, 657", "barbeiros": ["Thailo", "Jefferson", "Junior"]},
    "Unidade 2 - Bairro Boa Vista": {"end": "Rua Elvira Augusta, 203", "barbeiros": ["Davi", "Cabral"]}
}

# --- FUNÇÃO DE NOTIFICAÇÃO AUTOMÁTICA ---
def enviar_notificacao_automatica(msg):
    # Aqui você integraria com um serviço como Z-API ou Twilio
    # Por enquanto, o sistema registra isso internamente para o ADM
    if 'notificacoes_pendentes' not in st.
