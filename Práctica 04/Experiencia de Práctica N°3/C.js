// ÁMBITO DE FUNCIÓN

// Codigo
function exampleFunction() {
    const x = "declared inside function";
    console.log("Inside function");
    console.log(x);
}
console.log(x);

// Codigo
const x = "declared outside function";
exampleFunction();
function exampleFunction() {
    console.log("Inside function");
    console.log(x);
}
console.log("Outside function");
console.log(x);