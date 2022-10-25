from flask import Flask, render_template
app = Flask(__name__)

data = [
    {
        'element': 'Acerca de'
    },
    {
        'element': 'Nosotros'
    },
    {
        'element': 'Contacto'
    }

]

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', titulo='Agencia de Publicidad')

@app.route('/index2.html')
def arequipa():
    return render_template('index2.html')