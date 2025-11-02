import random

def simular_receber_mensagem():
    mensagens_demo = [
        'Olá, preciso de ajuda',
        'Qual é o horário de atendimento?',
        'Como posso enviar um documento?'
    ]
    return random.choice(mensagens_demo)
