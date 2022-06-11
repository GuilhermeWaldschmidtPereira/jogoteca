
from flask import Flask, redirect, render_template, request, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('League of Legends', 'Moba', 'PC')
jogo2 = Jogo('Overwatch', 'Tiro', 'PC/Xbox/PS')
jogo3 = Jogo('Fortnite', 'Tiro', 'PC/Xbox/PS')

lista_de_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key='guiwalper'


@app.route('/')
def index():


    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)

@app.route('/criar_jogo')
def criar_jogo():

    return render_template('novo_jogo.html', titulo='Novo jogo')
    

@app.route('/novo_jogo', methods=['POST'])
def novo_jogo():

    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)

    return redirect('/')

@app.route('/login')
def login():


    return render_template('login.html')

@app.route('/autenticar', methods=['POST', 'GET'])
def autenticar():

    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect('/')

    else:
        flash('Usuário não logado')
        return redirect('login')

app.run(debug=True, host='0.0.0.0', port=8080)
