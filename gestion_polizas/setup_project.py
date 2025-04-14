import os

def create_complete_project(base_dir):
    # Directorios principales
    dirs = [
        "backend/app",
        "backend/config",
        "backend/static",
        "backend/templates",
        "backend/app/services",
        "frontend/src/components",
        "frontend/src/utils",
        "frontend/public",
        "documentation",
        "deployment"
    ]

    # Archivos y contenido inicial
    files = {
        "backend/app/__init__.py": """# Inicialización de Flask
from flask import Flask

app = Flask(__name__)

# Configuración de la aplicación
app.config.from_object('config.settings')
""",
        "backend/app/models.py": """# Definición de base de datos y modelos
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Modelo de Empresa
class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
""",
        "backend/app/routes.py": """# Definición de rutas
from flask import Blueprint, jsonify
from .models import Empresa

routes = Blueprint('routes', __name__)

@routes.route('/companies', methods=['GET'])
def get_companies():
    return jsonify({'message': 'Empresas obtenidas'})
""",
        "backend/app/utils.py": """# Funciones auxiliares
def generar_alertas(notificaciones):
    print("Generando alertas...")
""",
        "backend/app/services/auth.py": """# Autenticación de usuarios
def autenticar_usuario():
    print("Autenticando usuario...")
""",
        "backend/app/services/alerts.py": """# Notificaciones automáticas
def enviar_alerta():
    print("Enviando alerta...")
""",
        "backend/config/settings.py": """# Configuración del sistema
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
""",
        "backend/run.py": """# Archivo principal
from app import app

if __name__ == '__main__':
    app.run(debug=True)
""",
        "frontend/src/App.jsx": """// Componente principal
import React from "react";
import Menu from "./components/Menu";

const App = () => (
    <div>
        <h1>Sistema de Notificaciones</h1>
        <Menu />
    </div>
);

export default App;
""",
        "frontend/src/utils/api.js": """// Funciones para consumir el API
import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:5000",
});

export default api;
""",
        "frontend/public/index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notificaciones</title>
</head>
<body>
    <div id="root"></div>
</body>
</html>
""",
        "frontend/package.json": """{
  "name": "noti-emp",
  "version": "1.0.0",
  "dependencies": {
    "react": "^18.0.0",
    "axios": "^1.0.0"
  }
}
""",
        "deployment/deploy.sh": """#!/bin/bash
echo "Iniciando despliegue en Firebase..."
cd ../frontend || exit
npm install
npm run build
cd ..
firebase deploy
echo "Despliegue completo."
""",
        "firebase.json": """{
  "hosting": {
    "public": "frontend/build",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
""",
        "documentation/README.md": """# Documentación del Proyecto
Este proyecto gestiona notificaciones para empresas con vencimientos programados.
"""
    }

    # Crear carpetas
    for dir in dirs:
        os.makedirs(os.path.join(base_dir, dir), exist_ok=True)

    # Crear archivos
    for file_path, content in files.items():
        full_path = os.path.join(base_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as file:
            file.write(content)

    print("Proyecto completo creado en:", base_dir)

# Ejecutar función
project_directory = "noti-emp"
create_complete_project(project_directory)
