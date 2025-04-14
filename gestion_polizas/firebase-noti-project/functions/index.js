const functions = require('firebase-functions');
const express = require('express');
const cors = require('cors');
const webpush = require('web-push');
const sqlite3 = require('sqlite3').verbose();

const app = express();
app.use(cors({ origin: true }));
app.use(express.json());

// Configuración para Web Push
webpush.setVapidDetails(
    'mailto:tu-correo@example.com', // Cambia por tu correo electrónico
    'TU_PUBLIC_VAPID_KEY',          // Clave pública generada
    'TU_PRIVATE_VAPID_KEY'          // Clave privada generada
);

// Inicializar la base de datos
const dbPath = './data/database.db';
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('Error al conectar con la base de datos:', err.message);
    } else {
        console.log('Conectado a la base de datos SQLite.');
    }
});

// Crear tablas si no existen
db.serialize(() => {
    db.run(`CREATE TABLE IF NOT EXISTS empresas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )`);

    db.run(`CREATE TABLE IF NOT EXISTS notificaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        empresa_id INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        mensaje TEXT NOT NULL,
        inicio DATE NOT NULL,
        vencimiento DATE NOT NULL,
        FOREIGN KEY (empresa_id) REFERENCES empresas (id)
    )`);

    db.run(`CREATE TABLE IF NOT EXISTS subscripciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        empresa_id INTEGER NOT NULL,
        endpoint TEXT NOT NULL,
        p256dh TEXT NOT NULL,
        auth TEXT NOT NULL,
        FOREIGN KEY (empresa_id) REFERENCES empresas (id)
    )`);
});

// Exportar la API como una función de Firebase
exports.api = functions.https.onRequest(app);
