# Portgas-Health

Portgas Health es un proyecto desarrollado con **Django**, orientado a la gestión de funcionalidades relacionadas con salud, ejercicio y administración de un gimnasio. El repositorio está organizado en varias aplicaciones internas que separan la lógica del sistema en módulos independientes.

---

## 📁 Estructura del proyecto

Portgas-Health/
├── ejercicio/        # App para gestión de ejercicios
├── gimnasio/         # App para gestión del gimnasio y sus recursos
├── receta/           # App para recetas o planes personalizados
├── portgas_health/   # Configuración principal del proyecto Django
├── manage.py         # Script principal de administración
└── README.md         # Documentación del proyecto

### 🧩 Apps incluidas

- **ejercicio** — Modelos y vistas relacionadas con ejercicios, rutinas o actividades físicas.
- **gimnasio** — Gestión del gimnasio: usuarios, clases, entrenadores, instalaciones, etc.
- **receta** — Módulo para recetas, planes alimenticios o recomendaciones personalizadas.
- **portgas_health** — Configuración base del proyecto (settings, URLs, WSGI/ASGI).

---

## 🚀 Requisitos

- Python 3.10+
- Django (versión instalada en tu entorno virtual)
- pip y venv

---

## 🔧 Instalación y ejecución

### 1. Crear y activar entorno virtual

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
