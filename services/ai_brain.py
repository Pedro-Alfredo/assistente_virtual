# services/ai_brain.py
import requests
from config import HUGGINGFACE_TOKEN, HF_MODEL, FALLBACK_ACTIVE

def gerar_resposta_online(mensagem):
    """Consulta a API da Hugging Face"""
    try:
        headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
        payload = {"inputs": mensagem, "parameters": {"max_new_tokens": 150}}
        resp = requests.post(f"https://api-inference.huggingface.co/models/{HF_MODEL}",
                             headers=headers, json=payload, timeout=20)
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, list) and "generated_text" in data[0]:
                return data[0]["generated_text"].strip()
            elif isinstance(data, dict) and "error" not in data:
                return str(data).strip()
        return None
    except Exception:
        return None

def gerar_resposta_offline(mensagem):
    """Fallback simples para respostas locais"""
    mensagem = mensagem.lower()
    if "horário" in mensagem or "atendimento" in mensagem:
        return "O horário de atendimento é das 8h às 17h, de segunda a sexta-feira."
    elif "olá" in mensagem or "bom dia" in mensagem:
        return "Olá! Em que posso ajudar hoje?"
    elif "documento" in mensagem or "imprimir" in mensagem:
        return "Posso preparar a sua carta ou documento. Envie os detalhes, por favor."
    else:
        return "Desculpe, não entendi. Poderia reformular sua pergunta?"

def responder(mensagem):
    resposta = gerar_resposta_online(mensagem)
    if not resposta and FALLBACK_ACTIVE:
        resposta = gerar_resposta_offline(mensagem)
    return resposta or "Desculpe, não consegui gerar uma resposta no momento."
