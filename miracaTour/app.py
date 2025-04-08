from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

guias = {
    "Carlos Lima": "carlos.turismo@gmail.com",
    "Ana Rios": "ana.rios@viagens.com",
    "Pedro Tour": "pedro@turismobr.com"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/destinos")
def destinos():
    lista_destinos = ["Rio de Janeiro", "Salvador", "Foz do Iguaçu", "Natal"]
    return render_template("destinos.html", destinos=lista_destinos)

@app.route("/passeios")
def passeios():
    passeios = {
        "Templo Budista Bunkyo": "Templo japonês em Registro - SP",
        "Salto de Biguá": "Cachoeira em Miracatu - SP",
        "Beira Mar": "Centro histórico em Cananeia - SP"
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

