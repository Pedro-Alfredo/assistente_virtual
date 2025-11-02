from flask import Flask, render_template, request, jsonify
from services.ai_brain import gerar_resposta
from services.whatsapp import simular_receber_mensagem

app = Flask(__name__)

mensagens = []

@app.route('/')
def dashboard():
    return render_template('dashboard.html', mensagens=mensagens)

@app.route('/enviar', methods=['POST'])
def enviar_mensagem():
    texto = request.form.get('mensagem')
    resposta = gerar_resposta(texto)
    mensagens.append({'de':'Usuário','texto': texto})
    mensagens.append({'de':'Assistente','texto': resposta})
    return jsonify({'resposta': resposta})

@app.route('/simular', methods=['POST'])
def simular_mensagem():
    texto = simular_receber_mensagem()
    resposta = gerar_resposta(texto)
    mensagens.append({'de':'Usuário','texto': texto})
    mensagens.append({'de':'Assistente','texto': resposta})
    return jsonify({'mensagem': texto, 'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)
