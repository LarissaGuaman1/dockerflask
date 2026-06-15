# Servicio Hola Mundo con Flask

Este proyecto crea un servicio sencillo con Flask usando Docker y Docker Compose.

## Estructura

```txt
holaflask_git/
├── .github/
│   └── workflows/
│       └── docker.yml
├── app.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Ejecutar localmente

```bash
docker compose up -d
```

Abrir en el navegador:

```txt
http://localhost:5000
```

## Detener el proyecto

```bash
docker compose down
```

## GitHub Actions

El archivo `.github/workflows/docker.yml` ejecuta una acción automática cuando se suben cambios a la rama `main`.

La acción realiza:

1. Descarga del código.
2. Construcción de la imagen Docker.
3. Verificación de que el proyecto puede construirse correctamente.
