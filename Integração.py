

from flask import flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/validar_login', methods=['POST'])
def validar():
    usuario = request.form['usuario']
    senha = request.form['senha']

    if usuario == 'admin' and senha == 'password':
        return redirect('/cadastro_livros')
    else:
        return "Login inválido! Tente novamente."

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
if __name__ == '__main__':
    app.run(debug=True)



