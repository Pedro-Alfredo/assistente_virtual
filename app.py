# app.py
from flask import Flask, render_template, request, jsonify
from services.ai_brain import responder

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensagem = data.get("mensagem", "")
    resposta = responder(mensagem)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
