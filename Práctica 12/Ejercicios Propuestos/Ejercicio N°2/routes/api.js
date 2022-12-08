const express = require('express');
const appRouter = express.Router();
var bodyParser = require('body-parser');

const con = require("../config/connection");

appRouter.use(bodyParser.urlencoded({
    extended: true
}));
appRouter.use(bodyParser.json());

let sql_all = `call listar_albums()`;

appRouter.get('/albums', verifiToken, (req, res) => {
    jwt.verify(req.token, 'secretkey', (err, authData) => {
        if (err) {
            res.json({
                mensaje: "Token no valido (expiro)",
            });
            res.sendStatus(403);
        } else {
            con.query(sql_all, (error, results) => {
                if (error) throw error;

                res.send(results[0]);
            });
        }
    });
});

let sql_insert = `call insertar_albums(?,?,?,?)`;

appRouter.post('/insertalbums', verifiToken, (req, res) => {
    jwt.verify(req.token, 'secretkey', (err, authData) => {
        if (err) {            
            res.json({
                mensaje: "Token no valido (expiro)",
            });
            res.sendStatus(403);
        } else {
            const album = {
                pTitulo: req.body.titulo,
                pLanzado: req.body.lanzado,
                pPrecio: req.body.precio,
                pGenero: req.body.genero
            };
            con.query(sql_insert, [album.pTitulo, album.pLanzado, album.pPrecio, album.pGenero]
                , (error, results) => {
                    if (error) throw error;

                    res.send(results[0]);
                });
        }
    });
});

const jwt = require('jsonwebtoken');

appRouter.post('/login', (req, res) => {
    const user = {
        id: 1,
        email: req.body.email,
        pass: req.body.pass,
    }
    jwt.sign({ user }, 'secretkey', { expiresIn: '120s' }, (err, token) => {
        res.json({
            tkn: 'bearer ' + token
        });
    });
});

function verifiToken(req, res, next) {
    const bearerHeader = req.headers['authorization'];
    if (typeof bearerHeader !== 'undefined') {
        const bearer = bearerHeader.split(' ');
        const bearerToken = bearer[1];
        req.token = bearerToken;
        next();
    } else {
        res.sendStatus(403);
    }
}

module.exports = appRouter;