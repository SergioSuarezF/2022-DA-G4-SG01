// Importando paquetes y archivos necesarios para crear estructura de documentos para colección

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var ProductSchema = new Schema(
	{
	name: String,
	amount: Number,
	description: String
	}
);

// ProductSchema.method("toJSON", function() {
//     const { __v, _id, ...object } = this.toObject();
//     object.id = _id;
//     return object;
//   });

module.exports = mongoose.model('products', ProductSchema);