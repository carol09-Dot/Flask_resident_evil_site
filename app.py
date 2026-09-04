from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/personagens")
def personagens():

    with open("data/personagens.json", "r", encoding="utf-8") as arquivo:
        personagens = json.load(arquivo)

    return render_template("personagens.html", personagens=personagens)

@app.route("/personagens/<int:id>")
def personagem_detalhes(id):

    with open("data/personagens.json", "r", encoding="utf-8") as arquivo:
        personagens = json.load(arquivo)

    for personagem in personagens:
        if personagem["id"] == id:
            return render_template(
                "personagem_detalhes.html",
                personagem=personagem
            )

    return "Personagem não encontrado", 404

@app.route("/viloes")
def viloes():

    with open("data/viloes.json", "r", encoding="utf-8") as arquivo:
        viloes = json.load(arquivo)

    return render_template("viloes.html", viloes=viloes)


@app.route("/viloes/<int:id>")
def vilao_detalhes(id):

    with open("data/viloes.json", "r", encoding="utf-8") as arquivo:
        viloes = json.load(arquivo)

    for vilao in viloes:
        if vilao["id"] == id:
            return render_template(
                "vilao_detalhes.html",
                vilao=vilao
            )

    return "Vilão não encontrado", 404

@app.route("/armas")
def armas():

    with open("data/armas.json", "r", encoding="utf-8") as arquivo:
        armas = json.load(arquivo)

    return render_template("armas.html", armas=armas)


@app.route("/armas/<int:id>")
def arma_detalhes(id):

    with open("data/armas.json", "r", encoding="utf-8") as arquivo:
        armas = json.load(arquivo)

    for arma in armas:
        if arma["id"] == id:
            return render_template(
                "arma_detalhes.html",
                arma=arma
            )

    return "Arma não encontrada", 404

@app.route("/jogos")
def jogos():

    with open("data/jogos.json", "r", encoding="utf-8") as arquivo:
        jogos = json.load(arquivo)

    return render_template("jogos.html", jogos=jogos)

@app.route("/jogos/<int:id>")
def jogo_detalhes(id):

    with open("data/jogos.json", "r", encoding="utf-8") as arquivo:
        jogos = json.load(arquivo)

    for jogo in jogos:
        if jogo["id"] == id:
            return render_template(
                "jogo_detalhes.html",
                jogo=jogo
            )

    return "Jogo não encontrado", 404

app.run(debug=True)
