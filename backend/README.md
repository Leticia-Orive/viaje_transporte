# Backend Python - Viajes y Transportes

API REST desarrollada con Flask para gestionar viajes y transportes.

## Instalación

1. Crear entorno virtual:
```bash
python -m venv venv
```

2. Activar entorno virtual:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Iniciar el servidor:
```bash
python app.py
```

2. El servidor estará disponible en `http://localhost:5000`

3. Inicializar la base de datos con datos de ejemplo:
```bash
POST http://localhost:5000/api/init-db
```

## Endpoints

### Transportes
- `GET /api/transportes` - Listar todos los transportes
- `GET /api/transportes/<id>` - Obtener un transporte
- `POST /api/transportes` - Crear transporte
- `PUT /api/transportes/<id>` - Actualizar transporte
- `DELETE /api/transportes/<id>` - Desactivar transporte

### Viajes
- `GET /api/viajes` - Listar todos los viajes
- `GET /api/viajes/<id>` - Obtener un viaje
- `GET /api/viajes/buscar?origen=X&destino=Y&fecha=Z` - Buscar viajes
- `POST /api/viajes` - Crear viaje
- `PUT /api/viajes/<id>` - Actualizar viaje
- `DELETE /api/viajes/<id>` - Eliminar viaje

### Reservas
- `GET /api/reservas` - Listar todas las reservas
- `GET /api/reservas/<id>` - Obtener una reserva
- `POST /api/reservas` - Crear reserva
- `PUT /api/reservas/<id>` - Actualizar reserva
- `DELETE /api/reservas/<id>` - Eliminar reserva
