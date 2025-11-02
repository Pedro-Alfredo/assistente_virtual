def gerar_resposta(mensagem):
    if 'olá' in mensagem.lower():
        return 'Olá! Como posso ajudar?'
    if 'ajuda' in mensagem.lower():
        return 'Claro, estou aqui para ajudar!'
    return 'Desculpe, não entendi. Pode reformular?'
