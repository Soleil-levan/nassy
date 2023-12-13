

document.addEventListener('DOMContentLoaded', function () {
    const chatBox = document.getElementById('chatBox');
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');

    const socket = io(); // Connexion au serveur WebSocket

    sendButton.addEventListener('click', function () {
        const message = messageInput.value;

        if (message.trim() !== '') {
            socket.emit('message', message); // Envoyer le message au serveur WebSocket
            messageInput.value = '';
        }
    });

    // Recevoir et afficher les messages du serveur WebSocket
    socket.on('message', function (message) {
        const messageElement = document.createElement('div');
        messageElement.textContent = message;
        chatBox.appendChild(messageElement);
    });
});

const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(express.static('public')); // Assure-toi que ton dossier public contient tes fichiers HTML, CSS, et script.js

io.on('connection', function (socket) {
    console.log('Nouvelle connexion WebSocket');

    // Écoute les messages du client
    socket.on('message', function (message) {
        // Diffuse le message à tous les clients connectés
        io.emit('message', message);
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, function () {
    console.log(`Serveur écoutant sur le port ${PORT}`);
});