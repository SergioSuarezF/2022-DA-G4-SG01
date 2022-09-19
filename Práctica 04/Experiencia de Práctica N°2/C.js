
   console.log(x === undefined); 
    var x = 3;

    var myvar = 'my value';
    (function() {
    console.log(myvar); 
    var myvar = 'valor local';
    })();
    console.log(myvar)
    console.log(x)