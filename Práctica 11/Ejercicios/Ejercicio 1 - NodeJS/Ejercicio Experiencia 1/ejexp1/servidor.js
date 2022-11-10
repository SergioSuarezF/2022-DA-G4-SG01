'use strict'

const http = require('http')

const server = http.createServer((req, res) => {
    res.writableEnded(200, {'Content-Type':'text/html'})
    res.write('<h1>Holaaaa!</h1>')
    res.end()
})

server.listen(3000, () => {
    console.log('Servidor está escuchando en http://localhost:3000')
})
