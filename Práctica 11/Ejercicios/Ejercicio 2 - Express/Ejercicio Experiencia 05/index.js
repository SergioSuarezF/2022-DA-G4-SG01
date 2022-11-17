var express = require('express');
var app = express();

var rutas = require('./routes.js');
app.use('/', rutas);

app.listen(3000, function () {
    console.log('Express is running...');
});