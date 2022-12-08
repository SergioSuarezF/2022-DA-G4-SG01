const express = require('express');
const app = express();
const cors = require('cors');

app.use(cors());

app.listen('5000',()=>{
    console.log("Servidor en Ejecucion");
})

const albumRouter = require('./routes/api');
app.use('/api',albumRouter);