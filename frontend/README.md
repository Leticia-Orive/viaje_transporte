# Frontend Angular - Sistema de Viajes y Transportes

Aplicación web desarrollada con Angular para gestionar viajes y reservas de transportes.

## Requisitos

- Node.js (v18 o superior)
- npm (v9 o superior)

## Instalación

1. Instalar dependencias:
```bash
cd frontend
npm install
```

## Desarrollo

Para ejecutar el servidor de desarrollo:

```bash
npm start
```

La aplicación estará disponible en `http://localhost:4200`

## Compilación

Para compilar el proyecto para producción:

```bash
npm run build
```

Los archivos compilados se guardarán en el directorio `dist/`.

## Estructura del Proyecto

```
src/
├── app/
│   ├── components/
│   │   ├── home/              # Página de inicio
│   │   ├── viajes-list/       # Lista y búsqueda de viajes
│   │   ├── reservas-list/     # Gestión de reservas
│   │   └── admin/             # Panel de administración
│   ├── services/              # Servicios para API
│   ├── models/                # Modelos de datos
│   ├── app.component.*        # Componente principal
│   ├── app.config.ts          # Configuración de la app
│   └── app.routes.ts          # Rutas de navegación
├── assets/                    # Recursos estáticos
├── styles.css                 # Estilos globales
└── index.html                 # HTML principal
```

## Características

- **Búsqueda de viajes**: Filtrar por origen, destino y fecha
- **Sistema de reservas**: Realizar reservas de forma sencilla
- **Panel de administración**: Gestionar transportes, viajes y reservas
- **Diseño responsive**: Compatible con dispositivos móviles
- **Interfaz moderna**: Diseño limpio y fácil de usar
