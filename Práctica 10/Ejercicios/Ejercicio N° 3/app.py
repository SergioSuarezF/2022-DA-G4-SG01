from flask import Flask,render_template, request, redirect
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sql'
 
mysql = MySQL(app)

@app.route('/ingresar')
def insert():
    return render_template('ingresar.html')

@app.route('/mostrar')
def select():
    return render_template('mostrar.html')

@app.route('/method', methods = ['POST', 'GET'])
def db2():     
    if request.method == 'POST':
        name = request.form['name']
        addy = request.form['addy']
        mail = request.form['mail']        
        password = request.form['password']
        date = request.form['date']
        gender = request.form['gender']
        election = request.form['election']
        aficiones = request.form['aficiones']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO persona VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''',(name, addy, mail, password, date, gender, election, aficiones))
        mysql.connection.commit()
        cursor.close()
        return redirect('/mostrar')
    
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM persona")
        data = cursor.fetchall()
        cursor.close()
        return render_template('select.html', data=data)