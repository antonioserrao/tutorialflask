from flask import Flask, render_template, g
import sqlite3


# configuração
DATABASE = 'banco.bd'
SECRET_KEY = '(y0(xtn@*19e8al$6^%3nb()l$0d=c$9akjb#j=+b5isr*sbuh' # numa app de verdade fica numa variável de ambiente com cerca de 1000 caracteres
#DEBUG = True
#USERNAME = 'admin'
#PASSWORD = 'default'


# app/serviço
app = Flask("Hello")
app.config.from_object(__name__)


def conecta_bd():
    return sqlite3.connect(DATABASE)

# Decorator para conectar ao BD
@app.before_request
def antes_requisicao():
    g.bd = conecta_bd()

#@app.after_request não funciona
@app.teardown_request
def depois_requisicao(e):
    g.bd.close()



## Decorator
#@app.route("/hello")
## Decorator
#@app.route("/")
#def hello():
#    return render_template("hello.html")
#
#
#@app.route("/sair")
#def tchau():
#    return "Sair!"

# Decorator
@app.route("/")
def exiber_entradas():
    nome = ["Antonio", "Geraldo", None, "Marta", "Luis"]
    sql = "SELECT titulo, texto, criado_em FROM entradas ORDER BY id DESC LIMIT(10);"
    cur = g.bd.execute(sql)

# Forma 01
    entradas = []
    for titulo, texto, criado_em in cur.fetchall():        
        entradas.append({"titulo":titulo, "texto":texto, "criado_em": criado_em})
# Forma 02
    #posts = [dict(titulo=titulo, texto=texto)
    #                for titulo, texto, criado_em in cur.fetchall()]
 # dicionatios exemplo:  #########
    # posts=[
    #    {"titulo": "Meu titulo", "texto":"Olá"},
    #    {"titulo": "Meu titulo", "texto":"Olá2"}
    #]
    
    return render_template("hello.html", entradas=entradas)


