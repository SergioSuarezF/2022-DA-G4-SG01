var mysql = require('mysql');

var con = mysql.createConnection({
    host:'localhost',
    database:'music',
    port:'3306',
    user:'root',
    password:'',
});

con.connect(function(err){
    if(err) throw err;
    console.log("Se conecto a la BD");
});

module.exports = con;