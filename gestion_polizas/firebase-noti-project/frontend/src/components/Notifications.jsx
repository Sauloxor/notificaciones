import React, { useState } from 'react';

const Notifications = () => {
    const [notifications, setNotifications] = useState([
        { id: 1, title: "Capacitaci�n", start: "", end: "" },
        { id: 2, title: "P�lizas de Seguro", start: "", end: "" },
        { id: 3, title: "Constancia de Seguridad Estructural", start: "", end: "" },
        { id: 4, title: "Dictamen de Seguridad y Operaci�n", start: "", end: "" },
        { id: 5, title: "Fumigaci�n", start: "", end: "" },
        { id: 6, title: "Alarma S�smica", start: "", end: "" }
    ]);

    const handleChange = (id, field, value) => {
        setNotifications(notifications.map(n => n.id === id ? { ...n, [field]: value } : n));
    };

    const handleSubmit = () => {
        console.log("Notificaciones seleccionadas:", notifications);
    };

    return (
        <div>
            <h2>Configurar Notificaciones</h2>
            {notifications.map(n => (
                <div key={n.id}>
                    <h3>{n.title}</h3>
                    <label>Inicio: </label>
                    <input type="date" value={n.start} onChange={(e) => handleChange(n.id, 'start', e.target.value)} />
                    <label>Vencimiento: </label>
                    <input type="date" value={n.end} onChange={(e) => handleChange(n.id, 'end', e.target.value)} />
                </div>
            ))}
            <button onClick={handleSubmit}>Guardar</button>
        </div>
    );
};

export default Notifications;
