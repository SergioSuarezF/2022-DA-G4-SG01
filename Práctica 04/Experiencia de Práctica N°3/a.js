// CIUDADANO DE PRIMERA CLASE 

// Codigo
const foo = () => {
    console.log("foobar");
}
foo();

// Fixed
const test = function () {
    console.log("hello");
}
test();

// Codigo
function sayHello() {
    return "Hello, ";
}
function greeting(helloMessage, name) {
    console.log(helloMessage() + name);
}
greeting(sayHello, "JavaScript!");