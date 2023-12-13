const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(express.static('../public'));

io.on('connection', function (socket) {
    console.log('Nouvelle connexion WebSocket');

    socket.on('message', function (message) {
        io.emit('message', message);
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, function () {
    console.log(`Serveur écoutant sur le port ${PORT}`);
});