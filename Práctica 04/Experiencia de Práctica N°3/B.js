// CLOSURE

// Codigo
function makeFunc() {
    const name = 'Mozilla';
    function displayName() {
        console.log(name);
    }
    return displayName;
}
const myFunc = makeFunc();
myFunc();

// Fixed
function test() {
    const text1 = 'Hello';
    const text2 = ' World!';
    function print() {
        console.log(text1 + text2);
    }
    return print;
}

const text = test();
text();