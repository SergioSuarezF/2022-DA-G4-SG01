var express = require('express');
var app = express();

const fecha = function (req, res, next) {
    req.fecha = Date.now()
    console.log('Timestamp: ', req.fecha);    
    next()
}
app.use(fecha)

app.get('/', (req, res) => {
    var fecha2 =  new Date(req.fecha)
    res.send('<h1>Bienvenido!</h1><br><h2>Fecha:</h2> ' + fecha2 + '<br><h2>En segundos:</h2> ' + req.fecha)
})


app.listen(3000, function () {
    console.log('Express is running...');
});