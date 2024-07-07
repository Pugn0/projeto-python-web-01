from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Samue", "membro_ativo": True},
        {"nome": "Maria", "membro_ativo": False},
        {"nome": "Laryssa", "membro_ativo": True}
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return """sobre"""

app.run(debug=True)