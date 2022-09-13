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

// Codigo
function f() {
    try {
        console.log(0);
        throw 'bogus';
    } catch (e) {
        console.log(1);
        return true;
        console.log(2);
    } finally {
        console.log(3);
        return false;
        console.log(4);
    }
    console.log(5);
}
console.log(f());