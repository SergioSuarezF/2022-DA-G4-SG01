var express = require('express');
var app = express();

var bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', function (req, res) {
    res.sendFile('index.html', { root: __dirname });
});

app.post('/registro', function (req, res) {
    var name = req.body.name;
    var mail = req.body.mail;
    var aficiones = req.body.aficiones;
    var election = req.body.election;
    var addy = req.body.addy;
    var gender = req.body.gender;
    var birth = req.body.birth;


    res.send('<h1>Datos registrados correctamente!</h1><br>Nombre Completo: ' + name + '<br>Direccion: ' + addy + '<br>Correo: ' + mail + '<br>Sexo: ' + gender + '<br>Fecha de Nacimiento: ' + birth + '<br>Aficiones' + aficiones + '<br>Temas de Interes' + election);
    // res.send('Gracias por registrarte, ' + name + '!');
});


app.listen(3000, function () {
    console.log('Express is running...');
});