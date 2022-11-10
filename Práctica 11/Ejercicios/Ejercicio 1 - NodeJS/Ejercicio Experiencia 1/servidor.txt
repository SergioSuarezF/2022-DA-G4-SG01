'use strict'

const http = require('http')
const PORT = process.env.PORT || 3000

const server = http.createServer((req, res) =>{
    res.writeHead(200, { 'Content-Type': 'text/html'})
    res.write('<h1>Welcome to my Web!!!</h1>')
    res.end()
})

server.listen(PORT, () => {
    console.log('Sergio Suarez is listening in http://localhost:${PORT}')
})