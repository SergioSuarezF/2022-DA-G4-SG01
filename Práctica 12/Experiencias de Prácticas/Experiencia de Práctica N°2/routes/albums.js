const express = require('express');
const appRouter = express.Router();
var bodyParser = require('body-parser');

const con = require("../config/connection");

appRouter.use(bodyParser.urlencoded({
    extended:true
}));
appRouter.use(bodyParser.json());

let sql_all = `call listar_albums()`;

appRouter.get('/albums', (req,res)=>{
    con.query(sql_all,(error, results)=>{
        if(error) throw error;

        res.send(results[0]);
    });
});


let sql_insert = `call insertar_albums(?,?,?,?)`;

appRouter.post('/insertalbums', (req,res)=>{
    const album = {
        pTitulo : req.body.titulo,
        pLanzado : req.body.lanzado,
        pPrecio : req.body.precio,
        pGenero : req.body.genero
    };
    con.query(sql_insert,[album.pTitulo,album.pLanzado,album.pPrecio,album.pGenero]
        ,(error, results)=>{
            if(error) throw error;

            res.send(results[0]);
        });
});


module.exports = appRouter;