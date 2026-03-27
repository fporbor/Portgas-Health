"""
Poblar la base de datos con datos de ejemplo.
Ejecución: python db.py
"""

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portgas_health.settings")  # ← cambia 'portgas' por el nombre de tu proyecto
django.setup()

from gimnasios.models import TipoGimnasio, Gimnasio  # ← cambia 'gimnasios' por el nombre de tu app

# ──────────────────────────────────────────────
# 1. Tipos de gimnasio
# ──────────────────────────────────────────────
tipos_data = [
    "Musculación y Fitness",
    "Crossfit",
    "Artes Marciales",
    "Yoga y Pilates",
    "Boxeo",
    "Natación",
]

tipos = {}
print("── Tipos de Gimnasio ─────────────────────────")
for nombre in tipos_data:
    obj, created = TipoGimnasio.objects.get_or_create(nombre=nombre)
    tipos[nombre] = obj
    estado = "Creado    " if created else "Ya existía"
    print(f"  [{estado}] {nombre}")

# ──────────────────────────────────────────────
# 2. Gimnasios
# ──────────────────────────────────────────────
gimnasios_data = [
    {
        "nombre": "FitZone Sevilla",
        "telefono": "954 123 456",
        "email": "info@fitzone-sevilla.es",
        "provincia": "Sevilla",
        "localidad": "Sevilla",
        "url": "https://www.fitzone-sevilla.es",
        "tipo_gimnasio": tipos["Musculación y Fitness"],
    },
    {
        "nombre": "CrossFit Triana",
        "telefono": "955 987 654",
        "email": "hola@crossfittriana.es",
        "provincia": "Sevilla",
        "localidad": "Triana",
        "url": "https://www.crossfittriana.es",
        "tipo_gimnasio": tipos["Crossfit"],
    },
    {
        "nombre": "Dojo Málaga",
        "telefono": "952 456 789",
        "email": "contacto@dojomalaga.es",
        "provincia": "Málaga",
        "localidad": "Málaga",
        "url": "https://www.dojomalaga.es",
        "tipo_gimnasio": tipos["Artes Marciales"],
    },
    {
        "nombre": "Zen Studio Granada",
        "telefono": "958 321 654",
        "email": "zen@zenstudiogranada.es",
        "provincia": "Granada",
        "localidad": "Granada",
        "url": "https://www.zenstudiogranada.es",
        "tipo_gimnasio": tipos["Yoga y Pilates"],
    },
    {
        "nombre": "Boxing Club Cádiz",
        "telefono": "956 741 852",
        "email": "info@boxingcadiz.es",
        "provincia": "Cádiz",
        "localidad": "Cádiz",
        "url": "https://www.boxingcadiz.es",
        "tipo_gimnasio": tipos["Boxeo"],
    },
    {
        "nombre": "Aqua Sport Córdoba",
        "telefono": "957 963 741",
        "email": "aqua@aquasportcordoba.es",
        "provincia": "Córdoba",
        "localidad": "Córdoba",
        "url": "https://www.aquasportcordoba.es",
        "tipo_gimnasio": tipos["Natación"],
    },
    {
        "nombre": "PowerGym Jerez",
        "telefono": "956 852 963",
        "email": "powergym@jerez.es",
        "provincia": "Cádiz",
        "localidad": "Jerez de la Frontera",
        "url": "https://www.powergymjerez.es",
        "tipo_gimnasio": tipos["Musculación y Fitness"],
    },
    {
        "nombre": "CrossFit Almería",
        "telefono": "950 147 258",
        "email": "info@crossfitalmeria.es",
        "provincia": "Almería",
        "localidad": "Almería",
        "url": "https://www.crossfitalmeria.es",
        "tipo_gimnasio": tipos["Crossfit"],
    },
]

print("\n── Gimnasios ─────────────────────────────────")
for data in gimnasios_data:
    obj, created = Gimnasio.objects.get_or_create(
        nombre=data["nombre"],
        defaults=data,
    )
    estado = "Creado    " if created else "Ya existía"
    print(f"  [{estado}] {obj}")

print("\n✅ Seed completado.")
print(f"   TipoGimnasio: {TipoGimnasio.objects.count()} registros")
print(f"   Gimnasio:     {Gimnasio.objects.count()} registros")