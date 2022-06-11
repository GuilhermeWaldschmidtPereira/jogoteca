
from flask import Flask, redirect, render_template, request, session, flash, url_for


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, nome, senha, nickname):
        self.nome = nome
        self.senha = senha
        self.nickname = nickname


jogo1 = Jogo('League of Legends', 'Moba', 'PC')
jogo2 = Jogo('Overwatch', 'Tiro', 'PC/Xbox/PS')
jogo3 = Jogo('Fortnite', 'Tiro', 'PC/Xbox/PS')

usuario1 = Usuario('Guilherme Waldschmidt', 'guiwalper', 'guiwalper')
usuario2 = Usuario('Ana Clara', 'clarinha', 'clarinha')
usuario3 = Usuario('Draven', 'draven', 'draven')

usuarios = {usuario1.nickname: usuario1,
            usuario2.nickname: usuario2,
            usuario3.nickname: usuario3}

lista_de_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'guiwalper'


@app.route('/')
def index():

    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)


@app.route('/criar_jogo')
def criar_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print(session)
        return redirect(url_for('login'))

    return render_template('novo_jogo.html', titulo='Novo jogo')


@app.route('/novo_jogo', methods=['POST'])
def novo_jogo():

    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)

    return redirect(url_for('index'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', 'GET'])
def autenticar():
    user_login =  request.form['usuario']
    if user_login in usuarios:
        if request.form['senha'] in usuarios[user_login].senha:

            session['usuario_logado'] = user_login
            flash(session['usuario_logado'] + ' logado com sucesso!')
            return redirect(url_for('index'))

    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!!')
    return redirect(url_for('login'))


app.run(debug=True, host='0.0.0.0', port=8080)
