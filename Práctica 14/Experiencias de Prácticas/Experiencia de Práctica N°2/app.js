
var admin = require("firebase-admin");
//////////////// USA TU KEY ///////////////////////
var serviceAccount = require("./servicekey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://da-ucsm-default-rtdb.firebaseio.com/"
});

// Escribir información en BD
var db = admin.database();
var ref = db.ref('server/data/nodejs');

var usersRef = ref.child("usuarios");
usersRef.set({
  alumnos : [{
    nombre:"joel",
    especialidad: "programados"
  },
  {
    nombre:"alonsito",
    especialidad: "analista"
  } ] 
});
