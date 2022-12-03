var express = require('express');
var app = express();
var bodyParser = require('body-parser');

const fs = require('firebase-admin');
const serviceAccount = require('./key.json');

// Cargando parámetros de Conexion con la BD
fs.initializeApp({
    credential: fs.credential.cert(serviceAccount)
});

// Conectarse a la BD y manejar errores
const db = fs.firestore();
const usersDb = db.collection('users');

// Configurando el Parser(conversor) de formato HTTP a formato JSON
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

// Creando Servidor
var server = app.listen(3000, "127.0.0.1", function () {
    var host = server.address().address;
    var port = server.address().port;
});

// Creando API
app.route('/users')
    .post(function (req, res) {
        console.log("/POST");
        var doc = req.body.doc;
        const usersDb = db.collection('users');
        usersDb.doc(doc).set({
            first: req.body.first,
            last: req.body.last,
            address: req.body.address,
            age: req.body.age,
            birthday: req.body.birthday
        });
        setTimeout(function () {
            var doc = req.body.doc;
            var document = db.collection("users").doc(doc);
            document.get().then((doc) => {
                if (doc.exists) {
                    // res.end(JSON.stringify(doc.data()));
                    res.json({ message: "Documento creado" });
                } else {
                    res.status(404).json({ error: "El documento no fue creado" });
                    // res.end("El documento no existe!");
                }
            }).catch((error) => {
                console.log(error);
            });
        }, 5000);
    })
    .get(function (req, res) {
        console.log("/GET");
        var doc = req.body.doc;
        var document = db.collection("users").doc(doc);

        document.get().then((doc) => {
            if (doc.exists) {
                res.end(JSON.stringify(doc.data()));
            } else {
                res.status(404).json({ error: "El documento no existe" });
                // res.end("El documento no existe!");
            }
        }).catch((error) => {
            console.log(error);
        });
    })
    .put(function (req, res) {
        console.log("/PUT");
        var docc = req.body.doc;
        var document = db.collection("users").doc(docc);
        document.get().then((doc) => {
            if (doc.exists) {
                db.collection('users').doc(docc).update({
                    first: req.body.first,
                    last: req.body.last,
                    address: req.body.address,
                    age: req.body.age,
                    birthday: req.body.birthday,
        
                });
                res.json({ message: "Documento actualizado" });
            } else {
                res.status(404).json({ error: "El documento no existe" });
                // res.end("El documento no existe!");
            }
        }).catch((error) => {
            console.log(error);
        });
    })
    .delete(function (req, res) {
        console.log("/DELETE");
        var docc = req.body.doc;
        var document = db.collection("users").doc(docc);

        document.get().then((doc) => {
            if (doc.exists) {
                db.collection('users').doc(docc).delete();
                res.json({ message: "Documento eliminado" });
            } else {
                res.status(404).json({ error: "El documento no existe" });
            }
        }).catch((error) => {
            console.log(error);
        });
    });