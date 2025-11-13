# Sistema de Viajes y Transportes

Proyecto completo de gestión de viajes y transportes con frontend en Angular y backend en Python (Flask).

## Estructura del Proyecto

```
viaje_transporte/
├── backend/           # API REST en Python Flask
│   ├── app.py        # Aplicación principal
│   ├── requirements.txt
│   └── README.md
├── frontend/         # Aplicación Angular
│   ├── src/
│   ├── package.json
│   └── README.md
└── README.md         # Este archivo
```

## Características

### Backend (Flask)
- API REST completa para gestionar transportes, viajes y reservas
- Base de datos SQLite
- CORS configurado para desarrollo
- Endpoints documentados

### Frontend (Angular)
- Búsqueda de viajes con filtros
- Sistema de reservas en tiempo real
- Panel de administración completo
- Diseño responsive y moderno
- Componentes standalone (Angular 17+)

## Instalación Rápida

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # En Windows
pip install -r requirements.txt
python app.py
```

El backend estará disponible en `http://localhost:5000`

### Frontend

```bash
cd frontend
npm install
npm start
```

El frontend estará disponible en `http://localhost:4200`

## Inicializar Base de Datos

Una vez que el backend esté corriendo, inicializa la base de datos con datos de ejemplo:

```bash
# Usando curl o Postman
POST http://localhost:5000/api/init-db
```

## Uso

1. **Iniciar Backend**: Ejecutar el servidor Flask
2. **Iniciar Frontend**: Ejecutar la aplicación Angular
3. **Inicializar DB**: Crear datos de ejemplo
4. **Acceder a la aplicación**: Abrir `http://localhost:4200`

## Páginas Disponibles

- **Inicio**: Página principal con información del sistema
- **Buscar Viajes**: Buscar y reservar viajes disponibles
- **Mis Reservas**: Ver y gestionar reservas
- **Administración**: Panel para gestionar transportes, viajes y reservas

## Tecnologías Utilizadas

### Backend
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- SQLite

### Frontend
- Angular 17+
- TypeScript
- RxJS
- CSS3

## Desarrollo

Para más detalles sobre el desarrollo de cada parte del proyecto, consultar los README específicos:
- [Backend README](backend/README.md)
- [Frontend README](frontend/README.md)

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.