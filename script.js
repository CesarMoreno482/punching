document.getElementById('registroForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const nombre = document.getElementById('nombre').value;
    registrarEntrada(nombre);
});

document.getElementById('agregarForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const nombre = document.getElementById('nombre').value;
    agregarNombre(nombre);
});

function registrarEntrada(nombre) {
    fetch('/api/entrada', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            cargarRegistros();
        } else {
            mostrarPopup(); // Mostrar el popup si el usuario no está registrado
        }
    });
}

function agregarNombre(nombre) {
    fetch('/api/agregar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert('Nombre agregado exitosamente.');
    });
}

function cargarRegistros() {
    fetch('/api/registros')
    .then(response => response.json())
    .then(data => {
        const lista = document.getElementById('listaRegistros');
        lista.innerHTML = '';
        data.forEach(registro => {
            const li = document.createElement('li');
            li.textContent = `${registro.nombre} - Entrada: ${registro.entrada}, Salida: ${registro.salida || 'No registrada'}`;
            lista.appendChild(li);
        });
    });
}

// Función para mostrar el popup cuando el usuario no esté registrado
function mostrarPopup() {
    const modal = document.getElementById('modalPopup');
    const span = document.getElementsByClassName('close')[0];

    modal.style.display = 'block';

    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    }
}

// Cargar registros al iniciar
cargarRegistros();
