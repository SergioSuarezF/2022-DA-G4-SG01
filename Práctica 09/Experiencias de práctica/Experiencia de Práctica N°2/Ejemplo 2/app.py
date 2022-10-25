from flask import Flask, render_template
app = Flask(__name__)

data = [
    {
        'pagina': 'Arequipa',
    },
    {
        'pagina': 'Cusco',
    },
    {
        'pagina': 'Piura',
    }

]

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', data=data)


@app.route('/arequipa.html')
def arequipa():
    return render_template('arequipa.html', data=data)


@app.route('/cusco.html')
def cusco():
    return render_template('cusco.html', data=data)


@app.route('/piura.html')
def piura():
    return render_template('piura.html', data=data)
