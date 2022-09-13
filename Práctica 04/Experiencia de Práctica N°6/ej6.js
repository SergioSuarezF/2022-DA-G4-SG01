console.log("Window");
console.log(window.location);
console.log(window.location.href);
console.log(window.location.hostname);
console.log(window.location.host);
console.log(window.location.pathname);
console.log(window.location.protocol);

setTimeout(function() {
    alert("¡ADVERTENCIA!");
    console.log("Potencial Virus");
}, 2000);
setInterval(function(){
    alert("¡FELICITACIONES!");
    console.log("Ganaste un auto 0km!");
}, 5000);
let referenciaObjetoVentana;
const strCaracteristicasVentana = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";
 
function myFunction() {
    var x = document.getElementById("myAnchor").href;
    document.getElementById("demo").innerHTML = x;
}

