from flask import Flask, render_template, request
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


def carregar_json(nome_arquivo):
    caminho = os.path.join(BASE_DIR, "data", nome_arquivo)

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


@app.route("/")
def inicio():
    return render_template("index.html")


# PERSONAGENS

@app.route("/personagens")
def personagens():
    personagens = carregar_json("personagens.json")

    return render_template(
        "personagens.html",
        personagens=personagens
    )


@app.route("/personagens/<int:id>")
def personagem_detalhes(id):
    personagens = carregar_json("personagens.json")

    for personagem in personagens:
        if personagem["id"] == id:
            return render_template(
                "personagem_detalhes.html",
                personagem=personagem
            )

    return "Personagem não encontrado", 404


# VILÕES

@app.route("/viloes")
def viloes():
    viloes = carregar_json("viloes.json")

    return render_template(
        "viloes.html",
        viloes=viloes
    )


@app.route("/viloes/<int:id>")
def vilao_detalhes(id):
    viloes = carregar_json("viloes.json")

    for vilao in viloes:
        if vilao["id"] == id:
            return render_template(
                "vilao_detalhes.html",
                vilao=vilao
            )

    return "Vilão não encontrado", 404


# ARMAS

@app.route("/armas")
def armas():
    armas = carregar_json("armas.json")

    return render_template(
        "armas.html",
        armas=armas
    )


@app.route("/armas/<int:id>")
def arma_detalhes(id):
    armas = carregar_json("armas.json")

    for arma in armas:
        if arma["id"] == id:
            return render_template(
                "arma_detalhes.html",
                arma=arma
            )

    return "Arma não encontrada", 404


# JOGOS

@app.route("/jogos")
def jogos():
    jogos = carregar_json("jogos.json")

    return render_template(
        "jogos.html",
        jogos=jogos
    )


@app.route("/jogos/<int:id>")
def jogo_detalhes(id):
    jogos = carregar_json("jogos.json")

    for jogo in jogos:
        if jogo["id"] == id:
            return render_template(
                "jogo_detalhes.html",
                jogo=jogo
            )

    return "Jogo não encontrado", 404


# AGENTES BIOLÓGICOS

@app.route("/virus")
def virus():
    virus = carregar_json("virus.json")

    return render_template(
        "virus.html",
        virus=virus
    )


@app.route("/virus/<int:id>")
def virus_detalhes(id):
    virus = carregar_json("virus.json")

    for item in virus:
        if item["id"] == id:
            return render_template(
                "virus_detalhes.html",
                virus=item
            )

    return "Agente biológico não encontrado", 404


# HISTÓRIA

@app.route("/historia")
def historia():
    return render_template("historia.html")


# PESQUISA

@app.route("/buscar")
def buscar():
    termo = request.args.get("q", "").lower()

    resultados = []

    arquivos = [
        ("personagens", "personagens.json"),
        ("viloes", "viloes.json"),
        ("armas", "armas.json"),
        ("jogos", "jogos.json"),
        ("virus", "virus.json")
    ]

    for categoria, nome_arquivo in arquivos:
        dados = carregar_json(nome_arquivo)

        for item in dados:
            if termo in item["nome"].lower():
                resultados.append({
                    "categoria": categoria,
                    "item": item
                })

    return render_template(
        "busca.html",
        resultados=resultados,
        termo=termo
    )


if __name__ == "__main__":
    app.run(debug=True)


