from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    pagina = {'data': 'Inicio'}
    usuario = {'data': 'Alonso'}
    emoji = {'data': '👋'}

    return render_template('index.html', title=pagina, user=usuario, emoji=emoji)
