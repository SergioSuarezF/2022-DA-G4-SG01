const express = require('express');
const cors = require('jsonwebtoken');
const app = express();


app.get('/api',function(req, res){
    res.json({
        mensaje: "Toma la data"
    });
});

app.post('/api/post', verifiToken, (req,res)=>{
    jwt.verify(req.token, 'secretkey', (err, authData)=>{
        if(err){
            res.sendStatus(403);
        }else{
            res.json({
                mensaje: "/POST",
                authData
            });
        }
    });
});

const jwt = require('jsonwebtoken');
app.post('/api/login', (req,res) => {
    const user = {
        id: 1,
        username: "joelyamir",
        email: "joel.pinto@ucsm.edu.pe",
    }
    jwt.sign({user}, 'secretkey', {expiresIn: '30s'},(err,token)=>{
        res.json({
            token
        });
    });
});

function verifiToken(req,res,next){
    const bearerHeader =  req.headers['authorization'];
    if(typeof bearerHeader !== 'undefined'){
        const bearer = bearerHeader.split(' ');
        const bearerToken = bearer[1];
        req.token = bearerToken;
        next();
    }else{
        res.sendStatus(403);
    }
}

app.listen(5000, () => console.log("Server running on port 5000..."));