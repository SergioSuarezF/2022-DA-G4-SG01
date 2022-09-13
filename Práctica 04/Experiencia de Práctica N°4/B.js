// AGREGANDO PROPIEDADES A LOS OBJETOS

// 1. Agregar propiedades a los objetos de a su proyecto utilizando iniciadores de objetos.
var libro1 = {
    titulo: 'In Search of Lost Time',
    autor: 'Marcel Proust',
    publicacion: 1913
}

// 2. Agregar objetos a su proyecto utilizando métodos constructores.
function libro(titulo, autor, publicacion) {
    this.titulo = titulo;
    this.autor = autor;
    this.publicacion = publicacion;
}

var libro2 = new libro('Ulysses', 'James Joyce', 1904);

//3. Agregar objetos a su proyecto utilizando el método object.create().
var libro3 = Object.create(libro1);
libro3.titulo = "Don Quixote";
libro3.autor = "Miguel de Cervantes";
libro3.publicacion = 1605;

console.log(libro1);
console.log(libro2);
console.log(libro3);