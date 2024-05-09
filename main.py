from flask import Flask, render_template, request

app= Flask(__name__)
@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    usuario = request.form['usuario']
    senha = request.form['senha']
    while True:
        if usuario == senha:
            mensagem = 'Usuário não pode ser igual a senha'
            return render_template('index.html', msg=mensagem)
        else:
            mensagem = 'Sucesso'
            return render_template('index.html', msg=mensagem)
            break

if (__name__) == ('__main__'):
    app.run(debug=True)
