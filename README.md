# 🏋️ Portgas Health

Aplicación web de salud y fitness desarrollada con **Django 5** y desplegada con **Docker**. Permite gestionar ejercicios, recetas y gimnasios, con un sistema de usuarios personalizado, likes y un chatbot integrado.

---

## 📋 Características

- **Ejercicios** — catálogo con tipo de ejercicio, grupo muscular y vídeo demostrativo.
- **Recetas** — recetas con información nutricional (proteínas, calorías), objetivo, alergias y vídeo demostrativo.
- **Gimnasios** — directorio de gimnasios con tipo, localización y foto.
- **Usuarios** — modelo de usuario extendido (segundo apellido, teléfono, fecha de nacimiento).
- **Sistema de likes** — los usuarios autenticados pueden dar like a ejercicios, recetas y gimnasios.
- **Mr. Portgas Bot** — chatbot flotante disponible en todas las páginas.
- **Panel de administración** Django para gestionar todos los modelos.

---

## 🛠️ Stack tecnológico

| Capa               | Tecnología              |
|--------------------|-------------------------|
| Backend            | Django 5 · Gunicorn     |
| Base de datos      | PostgreSQL 16           |
| Proxy inverso      | Nginx (Alpine)          |
| Contenerización    | Docker · Docker Compose |
| Archivos estáticos | WhiteNoise              |
| Configuración      | python-decouple         |

---

## 🚀 Puesta en marcha con Docker

### Prerrequisitos

- [Docker](https://docs.docker.com/get-docker/) ≥ 24
- [Docker Compose](https://docs.docker.com/compose/) ≥ 2

### 1. Clonar el repositorio

```bash
git clone https://github.com/fporbor/Portgas-Health.git
cd Portgas-Health
```

### 2. Configurar las variables de entorno

Crea un archivo `.env` en la raíz del proyecto (o edita el existente):

```env
DB_NAME=portgas
DB_USER=portgas
DB_PASSWORD=portgas
SECRET_KEY=cambia_esto_por_una_clave_secreta_segura
DEBUG=False
```

> ⚠️ En producción cambia `DEBUG=False` y usa una `SECRET_KEY` robusta.

### 3. Levantar los servicios

```bash
docker compose up --build
```

Esto ejecutará automáticamente las migraciones y recopilará los archivos estáticos.

### 4. Acceder a la aplicación

| Servicio                | URL                    |
|-------------------------|------------------------|
| Aplicación web          | http://localhost       |
| Panel de administración | http://localhost/admin |

### 5. Crear un superusuario (opcional)

```bash
docker compose exec web python manage.py createsuperuser
```

---

## 🗂️ Estructura del proyecto

```
portgas-health/
├── portgas_health/        # Configuración principal de Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── ejercicios/            # App de ejercicios
├── recetas/               # App de recetas
├── gimnasios/             # App de gimnasios
├── usuarios/              # App de usuarios y likes
├── templates/             # Plantillas HTML
├── static/                # CSS, JS e imágenes
├── media/                 # Archivos subidos por usuarios
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
└── requirements.txt
```

---

## 🧩 Aplicaciones Django

### `Usuarios`
Modelo `Usuario` extendido desde `AbstractUser`. Incluye segundo apellido, teléfono y fecha de nacimiento. También contiene el modelo genérico `Like`, que permite dar like a cualquier otro modelo del proyecto.

### `Ejercicios`
Modelo `Ejercicio` con nombre, descripción, tipo de ejercicio (hipertrofia, fuerza, resistencia…), grupo muscular (pecho, espalda, piernas…), vídeo y likes.

### `Recetas`
Modelo `Receta` con nombre, proteínas, calorías, objetivo nutricional, alergias, vídeo y likes.

### `Gimnasios`
Modelo `Gimnasio` con nombre, contacto, ubicación (provincia y localidad), enlace web, tipo de gimnasio y foto.

---

## ⚙️ Comandos útiles

```bash
# Ver los logs de todos los servicios
docker compose logs -f

# Ejecutar migraciones manualmente
docker compose exec web python manage.py migrate

# Abrir una shell de Django
docker compose exec web python manage.py shell

# Detener y eliminar los contenedores
docker compose down

# Detener y eliminar también los volúmenes (borra la BD)
docker compose down -v
```

---

## 📦 Dependencias principales

```
django>=5.0,<6.0
gunicorn>=21.0
psycopg2-binary>=2.9
whitenoise>=6.6
python-decouple>=3.8
django-extensions
```

---

## 🛜 Web Desplegada

```
https://portgas-health-production.up.railway.app/
```

## 📄 Licencia

Este proyecto es de uso educativo. Consulta el archivo `LICENSE` si existe, o contacta con los autores para más información.