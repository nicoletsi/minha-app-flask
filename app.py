
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Minha Aplicação Flask</title>
    </head>
    <body>
        <h1>Minha Aplicação Flask</h1>
        <p>Aplicação desenvolvida com Python e Flask.</p>
        <p>O back-end está funcionando!</p>
        <a href="/api/info">Consultar API</a>
    </body>
    </html>
    """

@app.route("/api/info")
def informacoes():
    return jsonify({
        "aplicacao": "Minha Aplicação Flask",
        "framework": "Flask",
        "linguagem": "Python",
        "mensagem": "API funcionando com sucesso!"
    })

if __name__ == "__main__":
    app.run(debug=True)
