from flask import Flask, render_template

app = Flask(__name__)

# criar primeira pagina no site
    # route + function
        # route -> caminho para a aopagina -> link apos dominio
        # function -> o que sera exibido em cada pagina
@app.route("/") # decorator
def homepage():
    return render_template("homepage.html")

@app.route("/sobrenos")
def sobrenos():
        return render_template("sobrenos.html")

# pagina dinamica
@app.route('/usuario/<nome>')
def usuarios(nome):
     return render_template("usuario.html", nome = nome)

# colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)