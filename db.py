"""
Poblar la base de datos con datos de ejemplo.
Ejecución: python db.py
"""

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portgas_health.settings")
django.setup()

from gimnasios.models import TipoGimnasio, Gimnasio
from ejercicios.models import TipoEjercicio, GrupoMuscular, Ejercicio
from recetas.models import Objetivo, Alergia, Receta

# ──────────────────────────────────────────────
# LIMPIAR BASE DE DATOS
# ──────────────────────────────────────────────
print("🧹 Limpiando base de datos...")

Receta.objects.all().delete()
Alergia.objects.all().delete()
Objetivo.objects.all().delete()

Ejercicio.objects.all().delete()
GrupoMuscular.objects.all().delete()
TipoEjercicio.objects.all().delete()

Gimnasio.objects.all().delete()
TipoGimnasio.objects.all().delete()

print("✅ Base de datos limpiada.\n")
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

# ──────────────────────────────────────────────
# 3. Tipos de ejercicio
# ──────────────────────────────────────────────
tipos_ejercicio_data = [
    "Hipertrofia",
    "Fuerza",
    "Resistencia",
    "Movilidad",
    "Cardio",
    "Rehabilitación",
]

tipos_ejercicio = {}
print("\n── Tipos de Ejercicio ────────────────────────")
for nombre in tipos_ejercicio_data:
    obj, created = TipoEjercicio.objects.get_or_create(nombre=nombre)
    tipos_ejercicio[nombre] = obj
    estado = "Creado    " if created else "Ya existía"
    print(f"  [{estado}] {nombre}")

# ──────────────────────────────────────────────
# 4. Grupos musculares
# ──────────────────────────────────────────────
grupos_data = [
    "Pecho",
    "Espalda",
    "Hombros",
    "Bíceps",
    "Tríceps",
    "Piernas",
    "Glúteos",
    "Abdomen",
    "Cardio",
]

grupos = {}
print("\n── Grupos Musculares ─────────────────────────")
for nombre in grupos_data:
    obj, created = GrupoMuscular.objects.get_or_create(nombre=nombre)
    grupos[nombre] = obj
    estado = "Creado    " if created else "Ya existía"
    print(f"  [{estado}] {nombre}")

# ──────────────────────────────────────────────
# 5. Ejercicios
# ──────────────────────────────────────────────
ejercicios_data = [
    {
        "nombre": "Press de banca",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Pecho", "Tríceps", "Hombros"],
        "descripcion": "Tumbado en un banco, baja la barra hasta el pecho y empuja hacia arriba.",
    },
    {
        "nombre": "Sentadilla",
        "tipo_ejercicio": tipos_ejercicio["Fuerza"],
        "grupos": ["Piernas", "Glúteos"],
        "descripcion": "Con la barra en la espalda, flexiona las rodillas hasta los 90° y sube.",
    },
    {
        "nombre": "Dominadas",
        "tipo_ejercicio": tipos_ejercicio["Fuerza"],
        "grupos": ["Espalda", "Bíceps"],
        "descripcion": "Cuelga de una barra y tira del cuerpo hacia arriba hasta que la barbilla supere la barra.",
    },
    {
        "nombre": "Press militar",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Hombros", "Tríceps"],
        "descripcion": "De pie o sentado, empuja la barra desde los hombros hacia arriba.",
    },
    {
        "nombre": "Peso muerto",
        "tipo_ejercicio": tipos_ejercicio["Fuerza"],
        "grupos": ["Espalda", "Piernas", "Glúteos"],
        "descripcion": "Desde el suelo, levanta la barra manteniendo la espalda recta.",
    },
    {
        "nombre": "Curl de bíceps",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Bíceps"],
        "descripcion": "Con mancuernas o barra, flexiona el codo llevando el peso hacia el hombro.",
    },
    {
        "nombre": "Plancha abdominal",
        "tipo_ejercicio": tipos_ejercicio["Resistencia"],
        "grupos": ["Abdomen"],
        "descripcion": "Apoyado en antebrazos y pies, mantén el cuerpo recto el mayor tiempo posible.",
    },
    {
        "nombre": "Carrera continua",
        "tipo_ejercicio": tipos_ejercicio["Cardio"],
        "grupos": ["Cardio", "Piernas"],
        "descripcion": "Correr a ritmo constante durante un tiempo determinado.",
    },
]

print("\n── Ejercicios ────────────────────────────────")
for data in ejercicios_data:
    obj, created = Ejercicio.objects.get_or_create(
        nombre=data["nombre"],
        defaults={
            "tipo_ejercicio": data["tipo_ejercicio"],
            "descripcion": data["descripcion"],
        },
    )
    obj.grupo_muscular.set([grupos[g] for g in data["grupos"]])
    estado = "Creado    " if created else "Ya existía"
    print(f"  [{estado}] {obj}")

# ──────────────────────────────────────────────
# 6. Objetivos
# ──────────────────────────────────────────────
objetivos_data = [
    "Pérdida de peso",
    "Ganancia muscular",
    "Mantenimiento",
    "Rendimiento deportivo",
    "Salud general",
]

objetivos = {}
print("\n── Objetivos ─────────────────────────────────")
for nombre in objetivos_data:
    obj, created = Objetivo.objects.get_or_create(nombre=nombre)
    objetivos[nombre] = obj
    estado = "Creado    " if created else "Ya existía"
    print(f"  [{estado}] {nombre}")

# ──────────────────────────────────────────────
# 7. Alergias
# ──────────────────────────────────────────────
alergias_data = [
    "Gluten",
    "Lactosa",
    "Huevo",
    "Frutos secos",
    "Soja",
    "Mariscos",
]

alergias = {}
print("\n── Alergias ──────────────────────────────────")
for nombre in alergias_data:
    obj, created = Alergia.objects.get_or_create(nombre=nombre)
    alergias[nombre] = obj
    estado = "Creado    " if created else "Ya existía"
    print(f"  [{estado}] {nombre}")

# ──────────────────────────────────────────────
# 8. Recetas
# ──────────────────────────────────────────────
recetas_data = [
    {
        "nombre": "Tortilla de avena con claras",
        "proteina": 30,
        "calorias": 320,
        "objetivo": objetivos["Ganancia muscular"],
        "alergias": ["Huevo", "Gluten"],
        "descripcion": "Mezcla copos de avena con claras de huevo y cocina en sartén antiadherente.",
    },
    {
        "nombre": "Ensalada de pollo y quinoa",
        "proteina": 40,
        "calorias": 450,
        "objetivo": objetivos["Mantenimiento"],
        "alergias": [],
        "descripcion": "Pechuga de pollo a la plancha con quinoa cocida, tomate y espinacas.",
    },
    {
        "nombre": "Batido proteico de plátano",
        "proteina": 35,
        "calorias": 380,
        "objetivo": objetivos["Ganancia muscular"],
        "alergias": ["Lactosa", "Soja"],
        "descripcion": "Plátano, proteína de suero, leche y mantequilla de cacahuete.",
    },
    {
        "nombre": "Salmón al horno con brócoli",
        "proteina": 45,
        "calorias": 420,
        "objetivo": objetivos["Pérdida de peso"],
        "alergias": ["Mariscos"],
        "descripcion": "Lomo de salmón con brócoli al vapor, ajo y aceite de oliva.",
    },
    {
        "nombre": "Bowl de arroz con legumbres",
        "proteina": 22,
        "calorias": 500,
        "objetivo": objetivos["Rendimiento deportivo"],
        "alergias": [],
        "descripcion": "Arroz integral con garbanzos, pimiento rojo y cúrcuma.",
    },
    {
        "nombre": "Yogur griego con frutos rojos",
        "proteina": 18,
        "calorias": 220,
        "objetivo": objetivos["Salud general"],
        "alergias": ["Lactosa"],
        "descripcion": "Yogur griego natural con arándanos, frambuesas y un chorrito de miel.",
    },
    {
        "nombre": "Tortitas de proteína",
        "proteina": 28,
        "calorias": 350,
        "objetivo": objetivos["Ganancia muscular"],
        "alergias": ["Gluten", "Huevo", "Lactosa"],
        "descripcion": "Harina de avena, huevo, proteína en polvo y leche. Cocinar en sartén.",
    },
    {
        "nombre": "Pechuga de pavo con boniato",
        "proteina": 42,
        "calorias": 410,
        "objetivo": objetivos["Pérdida de peso"],
        "alergias": [],
        "descripcion": "Pechuga de pavo a la plancha acompañada de boniato asado y judías verdes.",
    },
]

print("\n── Recetas ───────────────────────────────────")
for data in recetas_data:
    obj, created = Receta.objects.get_or_create(
        nombre=data["nombre"],
        defaults={
            "proteina": data["proteina"],
            "calorias": data["calorias"],
            "objetivo": data["objetivo"],
            "descripcion": data["descripcion"],
        },
    )
    obj.alergia.set([alergias[a] for a in data["alergias"]])
    estado = "Creado    " if created else "Ya existía"
    print(f"  [{estado}] {obj}")

# ──────────────────────────────────────────────
# Resumen
# ──────────────────────────────────────────────
print("\n✅ Seed completado.")
print(f"   TipoGimnasio:  {TipoGimnasio.objects.count()} registros")
print(f"   Gimnasio:      {Gimnasio.objects.count()} registros")
print(f"   TipoEjercicio: {TipoEjercicio.objects.count()} registros")
print(f"   GrupoMuscular: {GrupoMuscular.objects.count()} registros")
print(f"   Ejercicio:     {Ejercicio.objects.count()} registros")
print(f"   Objetivo:      {Objetivo.objects.count()} registros")
print(f"   Alergia:       {Alergia.objects.count()} registros")
print(f"   Receta:        {Receta.objects.count()} registros")