from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

destinos = {
    "Miracatu": "Terra de Gente Boa - R$2",
    "Cananéia": "Primeiro Povoado do Brasil - R$45",
    "Registro": "Marco da Colonização Japonesa em São Paulo - R$15",
    "Iguape": "Cidade Histórica no Vale do Ribeira - R$45"
}

passeios = {
    "Templo Budista Bunkyo": {
        "desc": "Templo japonês em Registro - SP",
        "img": "https://www.fotosedestinos.com/wp-content/uploads/2018/02/Templo-Budista-japon%C3%AAs-no-Hawaii-28-1280x720.jpg"
    },
    "Salto de Biguá": {
        "desc": "Cachoeira em Miracatu - SP",
        "img": "https://www.dondeandoporai.com.br/wp-content/uploads/2013/08/Cascata-della-Marmore-Terni-Italia.jpg"
    },
    "Beira Mar": {
        "desc": "Centro histórico em Cananeia - SP",
        "img": "https://media.tacdn.com/media/attractions-splice-spp-674x446/06/70/34/4f.jpg"
    },
    "Mirante do Cristo":{
        "desc": "Cristo de Iguape - SP",
        "img": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2d/ab/a0/bd/o-santuario-cristo-redentor.jpg?w=900&h=-1&s=1"
    },
    "Caverna do Diabo":{
        "desc": "Caverna em Eldorado - SP",
        "img": "https://cafeviagem.com/wp-content/uploads/2019/10/Gruta-Azul-Capri-1.jpg"
    }
}

guias = {
    "Carlos Lima": "carlos.turismo@gmail.com",
    "Ana Rios": "ana.rios@viagens.com",
    "Pedro Tour": "pedro@turismobr.com"
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/destinos", methods=["GET", "POST"])
def destinos_route():
    if request.method == "POST":
        nome = request.form.get("nome")
        desc = request.form.get("desc")
        if nome and desc:
            destinos[nome] = desc
    return render_template("destinos.html", destinos=destinos)


@app.route("/passeios", methods=["GET", "POST"])
def passeios_route():
    if request.method == "POST":
        nome = request.form.get("nome")
        desc = request.form.get("desc")
        img = request.form.get("img")
        if nome and desc and img:
            passeios[nome] = {
                "descricao": desc,
                "img": img
            }
    return render_template("passeios.html", passeios=passeios)


@app.route("/guias", methods=["GET", "POST"])
def guias_route():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        if nome and email:
            guias[nome] = email
    return render_template("guias.html", guias=guias)


if __name__ == "__main__":
    app.run(debug=True)
