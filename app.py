from flask import Flask, render_template

# Novo app/serviço
app = Flask("Hello")

# Decorator
@app.route("/hello")
# Decorator
@app.route("/")
def hello():
    return render_template("hello.html")


@app.route("/sair")
def tchau():
    return "Sair!"