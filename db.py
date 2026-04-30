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
    "Tradicional",
    "Crossfit",
    "Artes Marciales",
    "Otros",
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
    # A Coruña
    {"nombre": "BasicFit Coruña Centro", "telefono": "981 123 001", "email": "coruna1@basicfit.es", "provincia": "A Coruña", "localidad": "A Coruña", "url": "https://basicfit.es/coruna-centro", "tipo_gimnasio": "Tradicional"},
    {"nombre": "FitZone Santiago", "telefono": "981 123 002", "email": "santiago@fitzone.es", "provincia": "A Coruña", "localidad": "Santiago de Compostela", "url": "https://fitzone.es/santiago", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Arteixo", "telefono": "981 123 003", "email": "arteixo@dojo.es", "provincia": "A Coruña", "localidad": "Arteixo", "url": "https://dojo.es/arteixo", "tipo_gimnasio": "Artes Marciales"},

    # Lugo
    {"nombre": "VivaGym Lugo", "telefono": "982 123 001", "email": "lugo@vivagym.es", "provincia": "Lugo", "localidad": "Lugo", "url": "https://vivagym.es/lugo", "tipo_gimnasio": "Tradicional"},
    {"nombre": "Cross Lugo Box", "telefono": "982 123 002", "email": "crosslugo@box.es", "provincia": "Lugo", "localidad": "Monforte de Lemos", "url": "https://crosslugo.es", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Viveiro", "telefono": "982 123 003", "email": "viveiro@dojo.es", "provincia": "Lugo", "localidad": "Viveiro", "url": "https://dojo.es/viveiro", "tipo_gimnasio": "Artes Marciales"},

    # Ourense
    {"nombre": "AltaFit Ourense", "telefono": "988 123 001", "email": "ourense@altafit.es", "provincia": "Ourense", "localidad": "Ourense", "url": "https://altafit.es/ourense", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Ribeiro", "telefono": "988 123 002", "email": "ribeiro@crossfit.es", "provincia": "Ourense", "localidad": "Ribadavia", "url": "https://crossfit.es/ribeiro", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Verín", "telefono": "988 123 003", "email": "verin@dojo.es", "provincia": "Ourense", "localidad": "Verín", "url": "https://dojo.es/verin", "tipo_gimnasio": "Artes Marciales"},

    # Pontevedra
    {"nombre": "BasicFit Vigo", "telefono": "986 123 001", "email": "vigo@basicfit.es", "provincia": "Pontevedra", "localidad": "Vigo", "url": "https://basicfit.es/vigo", "tipo_gimnasio": "Tradicional"},
    {"nombre": "FitZone Pontevedra", "telefono": "986 123 002", "email": "pontevedra@fitzone.es", "provincia": "Pontevedra", "localidad": "Pontevedra", "url": "https://fitzone.es/pontevedra", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Lalín", "telefono": "986 123 003", "email": "lalin@dojo.es", "provincia": "Pontevedra", "localidad": "Lalín", "url": "https://dojo.es/lalin", "tipo_gimnasio": "Artes Marciales"},

    # Asturias
    {"nombre": "VivaGym Oviedo", "telefono": "985 123 001", "email": "oviedo@vivagym.es", "provincia": "Asturias", "localidad": "Oviedo", "url": "https://vivagym.es/oviedo", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Gijón", "telefono": "985 123 002", "email": "gijon@crossfit.es", "provincia": "Asturias", "localidad": "Gijón", "url": "https://crossfit.es/gijon", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Avilés", "telefono": "985 123 003", "email": "aviles@dojo.es", "provincia": "Asturias", "localidad": "Avilés", "url": "https://dojo.es/aviles", "tipo_gimnasio": "Artes Marciales"},

    # Cantabria
    {"nombre": "BasicFit Santander", "telefono": "942 123 001", "email": "santander@basicfit.es", "provincia": "Cantabria", "localidad": "Santander", "url": "https://basicfit.es/santander", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Torrelavega", "telefono": "942 123 002", "email": "torrelavega@crossfit.es", "provincia": "Cantabria", "localidad": "Torrelavega", "url": "https://crossfit.es/torrelavega", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Castro Urdiales", "telefono": "942 123 003", "email": "castro@dojo.es", "provincia": "Cantabria", "localidad": "Castro Urdiales", "url": "https://dojo.es/castro", "tipo_gimnasio": "Artes Marciales"},

    # Bizkaia
    {"nombre": "FitZone Bilbao", "telefono": "944 123 001", "email": "bilbao@fitzone.es", "provincia": "Bizkaia", "localidad": "Bilbao", "url": "https://fitzone.es/bilbao", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Barakaldo", "telefono": "944 123 002", "email": "barakaldo@crossfit.es", "provincia": "Bizkaia", "localidad": "Barakaldo", "url": "https://crossfit.es/barakaldo", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Getxo", "telefono": "944 123 003", "email": "getxo@dojo.es", "provincia": "Bizkaia", "localidad": "Getxo", "url": "https://dojo.es/getxo", "tipo_gimnasio": "Artes Marciales"},

    # Gipuzkoa
    {"nombre": "VivaGym Donostia", "telefono": "943 123 001", "email": "donostia@vivagym.es", "provincia": "Gipuzkoa", "localidad": "San Sebastián", "url": "https://vivagym.es/donostia", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Irún", "telefono": "943 123 002", "email": "irun@crossfit.es", "provincia": "Gipuzkoa", "localidad": "Irún", "url": "https://crossfit.es/irun", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Eibar", "telefono": "943 123 003", "email": "eibar@dojo.es", "provincia": "Gipuzkoa", "localidad": "Eibar", "url": "https://dojo.es/eibar", "tipo_gimnasio": "Artes Marciales"},

    # Álava
    {"nombre": "BasicFit Vitoria", "telefono": "945 123 001", "email": "vitoria@basicfit.es", "provincia": "Álava", "localidad": "Vitoria-Gasteiz", "url": "https://basicfit.es/vitoria", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Amurrio", "telefono": "945 123 002", "email": "amurrio@crossfit.es", "provincia": "Álava", "localidad": "Amurrio", "url": "https://crossfit.es/amurrio", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Laguardia", "telefono": "945 123 003", "email": "laguardia@dojo.es", "provincia": "Álava", "localidad": "Laguardia", "url": "https://dojo.es/laguardia", "tipo_gimnasio": "Artes Marciales"},

    # Navarra
    {"nombre": "FitZone Pamplona", "telefono": "948 123 001", "email": "pamplona@fitzone.es", "provincia": "Navarra", "localidad": "Pamplona", "url": "https://fitzone.es/pamplona", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Tudela", "telefono": "948 123 002", "email": "tudela@crossfit.es", "provincia": "Navarra", "localidad": "Tudela", "url": "https://crossfit.es/tudela", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Estella", "telefono": "948 123 003", "email": "estella@dojo.es", "provincia": "Navarra", "localidad": "Estella", "url": "https://dojo.es/estella", "tipo_gimnasio": "Artes Marciales"},

    # La Rioja
    {"nombre": "VivaGym Logroño", "telefono": "941 123 001", "email": "logrono@vivagym.es", "provincia": "La Rioja", "localidad": "Logroño", "url": "https://vivagym.es/logrono", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Haro", "telefono": "941 123 002", "email": "haro@crossfit.es", "provincia": "La Rioja", "localidad": "Haro", "url": "https://crossfit.es/haro", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Calahorra", "telefono": "941 123 003", "email": "calahorra@dojo.es", "provincia": "La Rioja", "localidad": "Calahorra", "url": "https://dojo.es/calahorra", "tipo_gimnasio": "Artes Marciales"},

    # Burgos
    {"nombre": "BasicFit Burgos", "telefono": "947 123 001", "email": "burgos@basicfit.es", "provincia": "Burgos", "localidad": "Burgos", "url": "https://basicfit.es/burgos", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Aranda", "telefono": "947 123 002", "email": "aranda@crossfit.es", "provincia": "Burgos", "localidad": "Aranda de Duero", "url": "https://crossfit.es/aranda", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Miranda", "telefono": "947 123 003", "email": "miranda@dojo.es", "provincia": "Burgos", "localidad": "Miranda de Ebro", "url": "https://dojo.es/miranda", "tipo_gimnasio": "Artes Marciales"},

    # León
    {"nombre": "FitZone León", "telefono": "987 123 001", "email": "leon@fitzone.es", "provincia": "León", "localidad": "León", "url": "https://fitzone.es/leon", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Ponferrada", "telefono": "987 123 002", "email": "ponferrada@crossfit.es", "provincia": "León", "localidad": "Ponferrada", "url": "https://crossfit.es/ponferrada", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Astorga", "telefono": "987 123 003", "email": "astorga@dojo.es", "provincia": "León", "localidad": "Astorga", "url": "https://dojo.es/astorga", "tipo_gimnasio": "Artes Marciales"},

    # Palencia
    {"nombre": "VivaGym Palencia", "telefono": "979 123 001", "email": "palencia@vivagym.es", "provincia": "Palencia", "localidad": "Palencia", "url": "https://vivagym.es/palencia", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Guardo", "telefono": "979 123 002", "email": "guardo@crossfit.es", "provincia": "Palencia", "localidad": "Guardo", "url": "https://crossfit.es/guardo", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Aguilar", "telefono": "979 123 003", "email": "aguilar@dojo.es", "provincia": "Palencia", "localidad": "Aguilar de Campoo", "url": "https://dojo.es/aguilar", "tipo_gimnasio": "Artes Marciales"},

    # Salamanca
    {"nombre": "BasicFit Salamanca", "telefono": "923 123 001", "email": "salamanca@basicfit.es", "provincia": "Salamanca", "localidad": "Salamanca", "url": "https://basicfit.es/salamanca", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Béjar", "telefono": "923 123 002", "email": "bejar@crossfit.es", "provincia": "Salamanca", "localidad": "Béjar", "url": "https://crossfit.es/bejar", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Ciudad Rodrigo", "telefono": "923 123 003", "email": "ciudadrodrigo@dojo.es", "provincia": "Salamanca", "localidad": "Ciudad Rodrigo", "url": "https://dojo.es/ciudadrodrigo", "tipo_gimnasio": "Artes Marciales"},

    # Segovia
    {"nombre": "FitZone Segovia", "telefono": "921 123 001", "email": "segovia@fitzone.es", "provincia": "Segovia", "localidad": "Segovia", "url": "https://fitzone.es/segovia", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Cuéllar", "telefono": "921 123 002", "email": "cuellar@crossfit.es", "provincia": "Segovia", "localidad": "Cuéllar", "url": "https://crossfit.es/cuellar", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo El Espinar", "telefono": "921 123 003", "email": "elespinar@dojo.es", "provincia": "Segovia", "localidad": "El Espinar", "url": "https://dojo.es/elespinar", "tipo_gimnasio": "Artes Marciales"},

    # Soria
    {"nombre": "VivaGym Soria", "telefono": "975 123 001", "email": "soria@vivagym.es", "provincia": "Soria", "localidad": "Soria", "url": "https://vivagym.es/soria", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Almazán", "telefono": "975 123 002", "email": "almazan@crossfit.es", "provincia": "Soria", "localidad": "Almazán", "url": "https://crossfit.es/almazan", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Ólvega", "telefono": "975 123 003", "email": "olvega@dojo.es", "provincia": "Soria", "localidad": "Ólvega", "url": "https://dojo.es/olvega", "tipo_gimnasio": "Artes Marciales"},

    # Valladolid
    {"nombre": "BasicFit Valladolid", "telefono": "983 123 001", "email": "valladolid@basicfit.es", "provincia": "Valladolid", "localidad": "Valladolid", "url": "https://basicfit.es/valladolid", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Medina", "telefono": "983 123 002", "email": "medina@crossfit.es", "provincia": "Valladolid", "localidad": "Medina del Campo", "url": "https://crossfit.es/medina", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Tordesillas", "telefono": "983 123 003", "email": "tordesillas@dojo.es", "provincia": "Valladolid", "localidad": "Tordesillas", "url": "https://dojo.es/tordesillas", "tipo_gimnasio": "Artes Marciales"},

    # Zamora
    {"nombre": "FitZone Zamora", "telefono": "980 123 001", "email": "zamora@fitzone.es", "provincia": "Zamora", "localidad": "Zamora", "url": "https://fitzone.es/zamora", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Benavente", "telefono": "980 123 002", "email": "benavente@crossfit.es", "provincia": "Zamora", "localidad": "Benavente", "url": "https://crossfit.es/benavente", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Toro", "telefono": "980 123 003", "email": "toro@dojo.es", "provincia": "Zamora", "localidad": "Toro", "url": "https://dojo.es/toro", "tipo_gimnasio": "Artes Marciales"},


    # Madrid
    {"nombre": "BasicFit Madrid Centro", "telefono": "910 123 001", "email": "madrid@basicfit.es", "provincia": "Madrid", "localidad": "Madrid", "url": "https://basicfit.es/madrid-centro", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Alcobendas", "telefono": "910 123 002", "email": "alcobendas@crossfit.es", "provincia": "Madrid", "localidad": "Alcobendas", "url": "https://crossfit.es/alcobendas", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Getafe", "telefono": "910 123 003", "email": "getafe@dojo.es", "provincia": "Madrid", "localidad": "Getafe", "url": "https://dojo.es/getafe", "tipo_gimnasio": "Artes Marciales"},

    # Toledo
    {"nombre": "FitZone Toledo", "telefono": "925 123 001", "email": "toledo@fitzone.es", "provincia": "Toledo", "localidad": "Toledo", "url": "https://fitzone.es/toledo", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Talavera", "telefono": "925 123 002", "email": "talavera@crossfit.es", "provincia": "Toledo", "localidad": "Talavera de la Reina", "url": "https://crossfit.es/talavera", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Illescas", "telefono": "925 123 003", "email": "illescas@dojo.es", "provincia": "Toledo", "localidad": "Illescas", "url": "https://dojo.es/illescas", "tipo_gimnasio": "Artes Marciales"},

    # Ciudad Real
    {"nombre": "VivaGym Ciudad Real", "telefono": "926 123 001", "email": "ciudadreal@vivagym.es", "provincia": "Ciudad Real", "localidad": "Ciudad Real", "url": "https://vivagym.es/ciudadreal", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Puertollano", "telefono": "926 123 002", "email": "puertollano@crossfit.es", "provincia": "Ciudad Real", "localidad": "Puertollano", "url": "https://crossfit.es/puertollano", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Valdepeñas", "telefono": "926 123 003", "email": "valdepenas@dojo.es", "provincia": "Ciudad Real", "localidad": "Valdepeñas", "url": "https://dojo.es/valdepenas", "tipo_gimnasio": "Artes Marciales"},

    # Cuenca
    {"nombre": "BasicFit Cuenca", "telefono": "969 123 001", "email": "cuenca@basicfit.es", "provincia": "Cuenca", "localidad": "Cuenca", "url": "https://basicfit.es/cuenca", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Tarancón", "telefono": "969 123 002", "email": "tarancon@crossfit.es", "provincia": "Cuenca", "localidad": "Tarancón", "url": "https://crossfit.es/tarancon", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Motilla", "telefono": "969 123 003", "email": "motilla@dojo.es", "provincia": "Cuenca", "localidad": "Motilla del Palancar", "url": "https://dojo.es/motilla", "tipo_gimnasio": "Artes Marciales"},

    # Guadalajara
    {"nombre": "FitZone Guadalajara", "telefono": "949 123 001", "email": "guadalajara@fitzone.es", "provincia": "Guadalajara", "localidad": "Guadalajara", "url": "https://fitzone.es/guadalajara", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Azuqueca", "telefono": "949 123 002", "email": "azuqueca@crossfit.es", "provincia": "Guadalajara", "localidad": "Azuqueca de Henares", "url": "https://crossfit.es/azuqueca", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Sigüenza", "telefono": "949 123 003", "email": "siguenca@dojo.es", "provincia": "Guadalajara", "localidad": "Sigüenza", "url": "https://dojo.es/siguenza", "tipo_gimnasio": "Artes Marciales"},

    # Ávila
    {"nombre": "VivaGym Ávila", "telefono": "920 123 001", "email": "avila@vivagym.es", "provincia": "Ávila", "localidad": "Ávila", "url": "https://vivagym.es/avila", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Arévalo", "telefono": "920 123 002", "email": "arevalo@crossfit.es", "provincia": "Ávila", "localidad": "Arévalo", "url": "https://crossfit.es/arevalo", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Candeleda", "telefono": "920 123 003", "email": "candeleda@dojo.es", "provincia": "Ávila", "localidad": "Candeleda", "url": "https://dojo.es/candeleda", "tipo_gimnasio": "Artes Marciales"},

    # Barcelona
    {"nombre": "BasicFit Barcelona Sants", "telefono": "931 123 001", "email": "barcelona@basicfit.es", "provincia": "Barcelona", "localidad": "Barcelona", "url": "https://basicfit.es/barcelona-sants", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Sabadell", "telefono": "931 123 002", "email": "sabadell@crossfit.es", "provincia": "Barcelona", "localidad": "Sabadell", "url": "https://crossfit.es/sabadell", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Mataró", "telefono": "931 123 003", "email": "mataro@dojo.es", "provincia": "Barcelona", "localidad": "Mataró", "url": "https://dojo.es/mataro", "tipo_gimnasio": "Artes Marciales"},

    # Girona
    {"nombre": "FitZone Girona", "telefono": "972 123 001", "email": "girona@fitzone.es", "provincia": "Girona", "localidad": "Girona", "url": "https://fitzone.es/girona", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Figueres", "telefono": "972 123 002", "email": "figueres@crossfit.es", "provincia": "Girona", "localidad": "Figueres", "url": "https://crossfit.es/figueres", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Blanes", "telefono": "972 123 003", "email": "blanes@dojo.es", "provincia": "Girona", "localidad": "Blanes", "url": "https://dojo.es/blanes", "tipo_gimnasio": "Artes Marciales"},

    # Lleida
    {"nombre": "VivaGym Lleida", "telefono": "973 123 001", "email": "lleida@vivagym.es", "provincia": "Lleida", "localidad": "Lleida", "url": "https://vivagym.es/lleida", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Tàrrega", "telefono": "973 123 002", "email": "tarrega@crossfit.es", "provincia": "Lleida", "localidad": "Tàrrega", "url": "https://crossfit.es/tarrega", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Balaguer", "telefono": "973 123 003", "email": "balaguer@dojo.es", "provincia": "Lleida", "localidad": "Balaguer", "url": "https://dojo.es/balaguer", "tipo_gimnasio": "Artes Marciales"},

    # Tarragona
    {"nombre": "BasicFit Tarragona", "telefono": "977 123 001", "email": "tarragona@basicfit.es", "provincia": "Tarragona", "localidad": "Tarragona", "url": "https://basicfit.es/tarragona", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Reus", "telefono": "977 123 002", "email": "reus@crossfit.es", "provincia": "Tarragona", "localidad": "Reus", "url": "https://crossfit.es/reus", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Amposta", "telefono": "977 123 003", "email": "amposta@dojo.es", "provincia": "Tarragona", "localidad": "Amposta", "url": "https://dojo.es/amposta", "tipo_gimnasio": "Artes Marciales"},

    # Castellón
    {"nombre": "BasicFit Castellón", "telefono": "964 123 001", "email": "castellon@basicfit.es", "provincia": "Castellón", "localidad": "Castellón de la Plana", "url": "https://basicfit.es/castellon", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Vila-real", "telefono": "964 123 002", "email": "vilareal@crossfit.es", "provincia": "Castellón", "localidad": "Vila-real", "url": "https://crossfit.es/vilareal", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Benicarló", "telefono": "964 123 003", "email": "benicarlo@dojo.es", "provincia": "Castellón", "localidad": "Benicarló", "url": "https://dojo.es/benicarlo", "tipo_gimnasio": "Artes Marciales"},

    # Valencia
    {"nombre": "FitZone Valencia Centro", "telefono": "963 123 001", "email": "valencia@fitzone.es", "provincia": "Valencia", "localidad": "Valencia", "url": "https://fitzone.es/valencia", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Gandía", "telefono": "963 123 002", "email": "gandia@crossfit.es", "provincia": "Valencia", "localidad": "Gandía", "url": "https://crossfit.es/gandia", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Torrent", "telefono": "963 123 003", "email": "torrent@dojo.es", "provincia": "Valencia", "localidad": "Torrent", "url": "https://dojo.es/torrent", "tipo_gimnasio": "Artes Marciales"},

    # Alicante
    {"nombre": "VivaGym Alicante", "telefono": "965 123 001", "email": "alicante@vivagym.es", "provincia": "Alicante", "localidad": "Alicante", "url": "https://vivagym.es/alicante", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Elche", "telefono": "965 123 002", "email": "elche@crossfit.es", "provincia": "Alicante", "localidad": "Elche", "url": "https://crossfit.es/elche", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Benidorm", "telefono": "965 123 003", "email": "benidorm@dojo.es", "provincia": "Alicante", "localidad": "Benidorm", "url": "https://dojo.es/benidorm", "tipo_gimnasio": "Artes Marciales"},

    # Murcia
    {"nombre": "BasicFit Murcia", "telefono": "968 123 001", "email": "murcia@basicfit.es", "provincia": "Murcia", "localidad": "Murcia", "url": "https://basicfit.es/murcia", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Cartagena", "telefono": "968 123 002", "email": "cartagena@crossfit.es", "provincia": "Murcia", "localidad": "Cartagena", "url": "https://crossfit.es/cartagena", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Lorca", "telefono": "968 123 003", "email": "lorca@dojo.es", "provincia": "Murcia", "localidad": "Lorca", "url": "https://dojo.es/lorca", "tipo_gimnasio": "Artes Marciales"},

    # Albacete
    {"nombre": "FitZone Albacete", "telefono": "967 123 001", "email": "albacete@fitzone.es", "provincia": "Albacete", "localidad": "Albacete", "url": "https://fitzone.es/albacete", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Hellín", "telefono": "967 123 002", "email": "hellin@crossfit.es", "provincia": "Albacete", "localidad": "Hellín", "url": "https://crossfit.es/hellin", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Villarrobledo", "telefono": "967 123 003", "email": "villarrobledo@dojo.es", "provincia": "Albacete", "localidad": "Villarrobledo", "url": "https://dojo.es/villarrobledo", "tipo_gimnasio": "Artes Marciales"},

    # Huelva
    {"nombre": "VivaGym Huelva", "telefono": "959 123 001", "email": "huelva@vivagym.es", "provincia": "Huelva", "localidad": "Huelva", "url": "https://vivagym.es/huelva", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Lepe", "telefono": "959 123 002", "email": "lepe@crossfit.es", "provincia": "Huelva", "localidad": "Lepe", "url": "https://crossfit.es/lepe", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Isla Cristina", "telefono": "959 123 003", "email": "islacristina@dojo.es", "provincia": "Huelva", "localidad": "Isla Cristina", "url": "https://dojo.es/islacristina", "tipo_gimnasio": "Artes Marciales"},

    # Sevilla
    {"nombre": "BasicFit Sevilla Nervión", "telefono": "954 123 001", "email": "sevilla@basicfit.es", "provincia": "Sevilla", "localidad": "Sevilla", "url": "https://basicfit.es/sevilla", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Dos Hermanas", "telefono": "954 123 002", "email": "doshermanas@crossfit.es", "provincia": "Sevilla", "localidad": "Dos Hermanas", "url": "https://crossfit.es/doshermanas", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Alcalá de Guadaíra", "telefono": "954 123 003", "email": "alcala@dojo.es", "provincia": "Sevilla", "localidad": "Alcalá de Guadaíra", "url": "https://dojo.es/alcala", "tipo_gimnasio": "Artes Marciales"},

    # Cádiz
    {"nombre": "FitZone Cádiz", "telefono": "956 123 001", "email": "cadiz@fitzone.es", "provincia": "Cádiz", "localidad": "Cádiz", "url": "https://fitzone.es/cadiz", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Jerez", "telefono": "956 123 002", "email": "jerez@crossfit.es", "provincia": "Cádiz", "localidad": "Jerez de la Frontera", "url": "https://crossfit.es/jerez", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Algeciras", "telefono": "956 123 003", "email": "algeciras@dojo.es", "provincia": "Cádiz", "localidad": "Algeciras", "url": "https://dojo.es/algeciras", "tipo_gimnasio": "Artes Marciales"},

    # Córdoba
    {"nombre": "VivaGym Córdoba", "telefono": "957 123 001", "email": "cordoba@vivagym.es", "provincia": "Córdoba", "localidad": "Córdoba", "url": "https://vivagym.es/cordoba", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Lucena", "telefono": "957 123 002", "email": "lucena@crossfit.es", "provincia": "Córdoba", "localidad": "Lucena", "url": "https://crossfit.es/lucena", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Puente Genil", "telefono": "957 123 003", "email": "puentegenil@dojo.es", "provincia": "Córdoba", "localidad": "Puente Genil", "url": "https://dojo.es/puentegenil", "tipo_gimnasio": "Artes Marciales"},

    # Málaga
    {"nombre": "BasicFit Málaga Centro", "telefono": "952 123 001", "email": "malaga@basicfit.es", "provincia": "Málaga", "localidad": "Málaga", "url": "https://basicfit.es/malaga", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Marbella", "telefono": "952 123 002", "email": "marbella@crossfit.es", "provincia": "Málaga", "localidad": "Marbella", "url": "https://crossfit.es/marbella", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Vélez-Málaga", "telefono": "952 123 003", "email": "velez@dojo.es", "provincia": "Málaga", "localidad": "Vélez-Málaga", "url": "https://dojo.es/velez", "tipo_gimnasio": "Artes Marciales"},

    # Jaén
    {"nombre": "FitZone Jaén", "telefono": "953 123 001", "email": "jaen@fitzone.es", "provincia": "Jaén", "localidad": "Jaén", "url": "https://fitzone.es/jaen", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Linares", "telefono": "953 123 002", "email": "linares@crossfit.es", "provincia": "Jaén", "localidad": "Linares", "url": "https://crossfit.es/linares", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Úbeda", "telefono": "953 123 003", "email": "ubeda@dojo.es", "provincia": "Jaén", "localidad": "Úbeda", "url": "https://dojo.es/ubeda", "tipo_gimnasio": "Artes Marciales"},

    # Granada
    {"nombre": "VivaGym Granada", "telefono": "958 123 001", "email": "granada@vivagym.es", "provincia": "Granada", "localidad": "Granada", "url": "https://vivagym.es/granada", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Motril", "telefono": "958 123 002", "email": "motril@crossfit.es", "provincia": "Granada", "localidad": "Motril", "url": "https://crossfit.es/motril", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Baza", "telefono": "958 123 003", "email": "baza@dojo.es", "provincia": "Granada", "localidad": "Baza", "url": "https://dojo.es/baza", "tipo_gimnasio": "Artes Marciales"},

    # Almería
    {"nombre": "BasicFit Almería", "telefono": "950 123 001", "email": "almeria@basicfit.es", "provincia": "Almería", "localidad": "Almería", "url": "https://basicfit.es/almeria", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Roquetas", "telefono": "950 123 002", "email": "roquetas@crossfit.es", "provincia": "Almería", "localidad": "Roquetas de Mar", "url": "https://crossfit.es/roquetas", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo El Ejido", "telefono": "950 123 003", "email": "elejido@dojo.es", "provincia": "Almería", "localidad": "El Ejido", "url": "https://dojo.es/elejido", "tipo_gimnasio": "Artes Marciales"},

    # Las Palmas
    {"nombre": "FitZone Las Palmas", "telefono": "928 123 001", "email": "laspalmas@fitzone.es", "provincia": "Las Palmas", "localidad": "Las Palmas de Gran Canaria", "url": "https://fitzone.es/laspalmas", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Telde", "telefono": "928 123 002", "email": "telde@crossfit.es", "provincia": "Las Palmas", "localidad": "Telde", "url": "https://crossfit.es/telde", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Arrecife", "telefono": "928 123 003", "email": "arrecife@dojo.es", "provincia": "Las Palmas", "localidad": "Arrecife", "url": "https://dojo.es/arrecife", "tipo_gimnasio": "Artes Marciales"},

    # Santa Cruz de Tenerife
    {"nombre": "VivaGym Tenerife", "telefono": "922 123 001", "email": "tenerife@vivagym.es", "provincia": "Santa Cruz de Tenerife", "localidad": "Santa Cruz de Tenerife", "url": "https://vivagym.es/tenerife", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit La Laguna", "telefono": "922 123 002", "email": "laguna@crossfit.es", "provincia": "Santa Cruz de Tenerife", "localidad": "San Cristóbal de La Laguna", "url": "https://crossfit.es/laguna", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Adeje", "telefono": "922 123 003", "email": "adeje@dojo.es", "provincia": "Santa Cruz de Tenerife", "localidad": "Adeje", "url": "https://dojo.es/adeje", "tipo_gimnasio": "Artes Marciales"},

    # Illes Balears
    {"nombre": "BasicFit Palma", "telefono": "971 123 001", "email": "palma@basicfit.es", "provincia": "Illes Balears", "localidad": "Palma de Mallorca", "url": "https://basicfit.es/palma", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Manacor", "telefono": "971 123 002", "email": "manacor@crossfit.es", "provincia": "Illes Balears", "localidad": "Manacor", "url": "https://crossfit.es/manacor", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Ibiza", "telefono": "971 123 003", "email": "ibiza@dojo.es", "provincia": "Illes Balears", "localidad": "Ibiza", "url": "https://dojo.es/ibiza", "tipo_gimnasio": "Artes Marciales"},

    # Zaragoza
    {"nombre": "FitZone Zaragoza", "telefono": "976 123 001", "email": "zaragoza@fitzone.es", "provincia": "Zaragoza", "localidad": "Zaragoza", "url": "https://fitzone.es/zaragoza", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Calatayud", "telefono": "976 123 002", "email": "calatayud@crossfit.es", "provincia": "Zaragoza", "localidad": "Calatayud", "url": "https://crossfit.es/calatayud", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Ejea", "telefono": "976 123 003", "email": "ejea@dojo.es", "provincia": "Zaragoza", "localidad": "Ejea de los Caballeros", "url": "https://dojo.es/ejea", "tipo_gimnasio": "Artes Marciales"},

    # Huesca
    {"nombre": "VivaGym Huesca", "telefono": "974 123 001", "email": "huesca@vivagym.es", "provincia": "Huesca", "localidad": "Huesca", "url": "https://vivagym.es/huesca", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Jaca", "telefono": "974 123 002", "email": "jaca@crossfit.es", "provincia": "Huesca", "localidad": "Jaca", "url": "https://crossfit.es/jaca", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Monzón", "telefono": "974 123 003", "email": "monzon@dojo.es", "provincia": "Huesca", "localidad": "Monzón", "url": "https://dojo.es/monzon", "tipo_gimnasio": "Artes Marciales"},

    # Teruel
    {"nombre": "BasicFit Teruel", "telefono": "978 123 001", "email": "teruel@basicfit.es", "provincia": "Teruel", "localidad": "Teruel", "url": "https://basicfit.es/teruel", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Alcañiz", "telefono": "978 123 002", "email": "alcaniz@crossfit.es", "provincia": "Teruel", "localidad": "Alcañiz", "url": "https://crossfit.es/alcaniz", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Andorra", "telefono": "978 123 003", "email": "andorra@dojo.es", "provincia": "Teruel", "localidad": "Andorra", "url": "https://dojo.es/andorra", "tipo_gimnasio": "Artes Marciales"},

    # Ceuta
    {"nombre": "FitZone Ceuta", "telefono": "956 123 101", "email": "ceuta@fitzone.es", "provincia": "Ceuta", "localidad": "Ceuta", "url": "https://fitzone.es/ceuta", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Ceuta Box", "telefono": "956 123 102", "email": "ceutabox@crossfit.es", "provincia": "Ceuta", "localidad": "Ceuta", "url": "https://crossfit.es/ceuta", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Ceuta Este", "telefono": "956 123 103", "email": "ceutaeste@dojo.es", "provincia": "Ceuta", "localidad": "Ceuta", "url": "https://dojo.es/ceutaeste", "tipo_gimnasio": "Artes Marciales"},

    # Melilla
    {"nombre": "VivaGym Melilla", "telefono": "952 123 101", "email": "melilla@vivagym.es", "provincia": "Melilla", "localidad": "Melilla", "url": "https://vivagym.es/melilla", "tipo_gimnasio": "Tradicional"},
    {"nombre": "CrossFit Melilla", "telefono": "952 123 102", "email": "melilla@crossfit.es", "provincia": "Melilla", "localidad": "Melilla", "url": "https://crossfit.es/melilla", "tipo_gimnasio": "Crossfit"},
    {"nombre": "Dojo Melilla Norte", "telefono": "952 123 103", "email": "melillanorte@dojo.es", "provincia": "Melilla", "localidad": "Melilla", "url": "https://dojo.es/melillanorte", "tipo_gimnasio": "Artes Marciales"},

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
    "Core",
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
        "descripcion": "Tumbado en un banco, baja la barra al pecho y empuja explosivamente hacia arriba.",
    },
    {
        "nombre": "Sentadilla con barra",
        "tipo_ejercicio": tipos_ejercicio["Fuerza"],
        "grupos": ["Piernas", "Glúteos", "Core"],
        "descripcion": "Flexiona las rodillas manteniendo la espalda recta y sube empujando con las piernas.",
    },
    {
        "nombre": "Peso muerto",
        "tipo_ejercicio": tipos_ejercicio["Fuerza"],
        "grupos": ["Espalda", "Piernas", "Glúteos"],
        "descripcion": "Levanta la barra desde el suelo manteniendo la espalda neutra y el core firme.",
    },
    {
        "nombre": "Dominadas",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Espalda", "Bíceps"],
        "descripcion": "Suspéndete de la barra y eleva tu cuerpo hasta que la barbilla supere la barra.",
    },
    {
        "nombre": "Press militar",
        "tipo_ejercicio": tipos_ejercicio["Fuerza"],
        "grupos": ["Hombros", "Tríceps"],
        "descripcion": "Empuja la barra por encima de la cabeza manteniendo el core firme.",
    },
    {
        "nombre": "Curl de bíceps con mancuernas",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Bíceps"],
        "descripcion": "Flexiona los codos levantando las mancuernas sin balancear el cuerpo.",
    },
    {
        "nombre": "Extensión de tríceps en polea",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Tríceps"],
        "descripcion": "Empuja la cuerda hacia abajo extendiendo completamente los codos.",
    },
    {
        "nombre": "Remo con barra",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Espalda", "Bíceps"],
        "descripcion": "Inclina el torso y lleva la barra hacia el Core manteniendo la espalda recta.",
    },
    {
        "nombre": "Zancadas",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Piernas", "Glúteos"],
        "descripcion": "Da un paso largo hacia adelante y baja la rodilla trasera hacia el suelo.",
    },
    {
        "nombre": "Elevaciones laterales",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Hombros"],
        "descripcion": "Eleva las mancuernas hacia los lados hasta la altura de los hombros.",
    },

    # 11–20
    {
        "nombre": "Plancha abdominal",
        "tipo_ejercicio": tipos_ejercicio["Resistencia"],
        "grupos": ["Core"],
        "descripcion": "Mantén el cuerpo recto apoyado en antebrazos y puntas de los pies.",
    },
    {
        "nombre": "Mountain climbers",
        "tipo_ejercicio": tipos_ejercicio["Cardio"],
        "grupos": ["Core", "Piernas"],
        "descripcion": "Alterna rodillas al pecho rápidamente en posición de plancha.",
    },
    {
        "nombre": "Burpees",
        "tipo_ejercicio": tipos_ejercicio["Cardio"],
        "grupos": ["Pecho", "Piernas", "Core"],
        "descripcion": "Salta, baja al suelo, haz una flexión y vuelve a saltar.",
    },
    {
        "nombre": "Flexiones",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Pecho", "Tríceps", "Hombros"],
        "descripcion": "Empuja el suelo extendiendo los brazos desde posición de plancha.",
    },
    {
        "nombre": "Jalón al pecho",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Espalda", "Bíceps"],
        "descripcion": "Tira de la barra hacia el pecho manteniendo el torso estable.",
    },
    {
        "nombre": "Press inclinado con mancuernas",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Pecho", "Hombros"],
        "descripcion": "Empuja las mancuernas hacia arriba en un banco inclinado.",
    },
    {
        "nombre": "Peso muerto rumano",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Espalda", "Glúteos", "Piernas"],
        "descripcion": "Desciende la barra con ligera flexión de rodillas manteniendo la espalda recta.",
    },
    {
        "nombre": "Saltos al cajón",
        "tipo_ejercicio": tipos_ejercicio["Cardio"],
        "grupos": ["Piernas", "Glúteos"],
        "descripcion": "Salta explosivamente sobre un cajón y baja controlado.",
    },
    {
        "nombre": "Remo en polea baja",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Espalda", "Bíceps"],
        "descripcion": "Tira del agarre hacia el Core manteniendo el pecho erguido.",
    },
    {
        "nombre": "Press francés",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Tríceps"],
        "descripcion": "Extiende los codos llevando la barra desde detrás de la cabeza.",
    },

    # 21–30
    {
        "nombre": "Bicicleta estática",
        "tipo_ejercicio": tipos_ejercicio["Cardio"],
        "grupos": ["Piernas"],
        "descripcion": "Pedalea manteniendo una intensidad constante o por intervalos.",
    },
    {
        "nombre": "Cinta de correr",
        "tipo_ejercicio": tipos_ejercicio["Cardio"],
        "grupos": ["Piernas"],
        "descripcion": "Corre o camina a diferentes velocidades e inclinaciones.",
    },
    {
        "nombre": "Remo ergómetro",
        "tipo_ejercicio": tipos_ejercicio["Cardio"],
        "grupos": ["Espalda", "Piernas", "Core"],
        "descripcion": "Tira del agarre mientras impulsas con las piernas.",
    },
    {
        "nombre": "Face pulls",
        "tipo_ejercicio": tipos_ejercicio["Rehabilitación"],
        "grupos": ["Hombros", "Espalda"],
        "descripcion": "Tira de la cuerda hacia la cara para fortalecer rotadores externos.",
    },
    {
        "nombre": "Paseo del granjero",
        "tipo_ejercicio": tipos_ejercicio["Fuerza"],
        "grupos": ["Core", "Hombros", "Piernas"],
        "descripcion": "Camina cargando pesadas mancuernas a cada lado.",
    },
    {
        "nombre": "Hip thrust",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Glúteos", "Piernas"],
        "descripcion": "Eleva la cadera empujando con los glúteos.",
    },
    {
        "nombre": "Aperturas con mancuernas",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Pecho"],
        "descripcion": "Abre los brazos en arco manteniendo ligera flexión de codos.",
    },
    {
        "nombre": "Press Arnold",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Hombros"],
        "descripcion": "Gira las mancuernas mientras las elevas por encima de la cabeza.",
    },
    {
        "nombre": "Gemelos de pie",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Piernas"],
        "descripcion": "Eleva los talones manteniendo las rodillas extendidas.",
    },
    {
        "nombre": "Encogimientos abdominales",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Core"],
        "descripcion": "Eleva el torso contrayendo el Core.",
    },

    # 31–40
    {
        "nombre": "Press de piernas",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Piernas", "Glúteos"],
        "descripcion": "Empuja la plataforma extendiendo las piernas sin bloquear rodillas.",
    },
    {
        "nombre": "Jalón tras nuca",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Espalda"],
        "descripcion": "Tira de la barra hacia detrás de la cabeza con control.",
    },
    {
        "nombre": "Rotaciones de tronco",
        "tipo_ejercicio": tipos_ejercicio["Movilidad"],
        "grupos": ["Core"],
        "descripcion": "Gira el torso suavemente para mejorar movilidad lumbar.",
    },
    {
        "nombre": "Estiramiento de isquios",
        "tipo_ejercicio": tipos_ejercicio["Movilidad"],
        "grupos": ["Piernas"],
        "descripcion": "Inclínate hacia adelante manteniendo las piernas estiradas.",
    },
    {
        "nombre": "Elevaciones frontales",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Hombros"],
        "descripcion": "Eleva las mancuernas hacia adelante hasta la altura de los hombros.",
    },
    {
        "nombre": "Press cerrado",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Pecho", "Tríceps"],
        "descripcion": "Empuja la barra con agarre estrecho para enfatizar tríceps.",
    },
    {
        "nombre": "Remo con mancuerna a una mano",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Espalda", "Bíceps"],
        "descripcion": "Tira de la mancuerna hacia la cadera manteniendo el torso estable.",
    },
    {
        "nombre": "Saltos de tijera",
        "tipo_ejercicio": tipos_ejercicio["Cardio"],
        "grupos": ["Piernas"],
        "descripcion": "Alterna saltos abriendo y cerrando piernas y brazos.",
    },
    {
        "nombre": "Press Pallof",
        "tipo_ejercicio": tipos_ejercicio["Rehabilitación"],
        "grupos": ["Core"],
        "descripcion": "Resiste la rotación del tronco empujando la polea hacia adelante.",
    },
    {
        "nombre": "Extensión lumbar",
        "tipo_ejercicio": tipos_ejercicio["Rehabilitación"],
        "grupos": ["Espalda"],
        "descripcion": "Extiende la espalda desde un banco romano para fortalecer lumbares.",
    },

    # 41–50
    {
        "nombre": "Sprints",
        "tipo_ejercicio": tipos_ejercicio["Cardio"],
        "grupos": ["Piernas"],
        "descripcion": "Corre a máxima velocidad en intervalos cortos.",
    },
    {
        "nombre": "Farmer carry unilateral",
        "tipo_ejercicio": tipos_ejercicio["Fuerza"],
        "grupos": ["Core", "Hombros"],
        "descripcion": "Camina cargando peso solo en un lado para trabajar estabilidad.",
    },
    {
        "nombre": "Press de pecho en máquina",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Pecho"],
        "descripcion": "Empuja las asas hacia adelante manteniendo control del movimiento.",
    },
    {
        "nombre": "Remo invertido",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Espalda", "Bíceps"],
        "descripcion": "Tira del pecho hacia la barra manteniendo el cuerpo recto.",
    },
    {
        "nombre": "Sentadilla búlgara",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Piernas", "Glúteos"],
        "descripcion": "Apoya un pie atrás y baja controlado sobre la pierna delantera.",
    },
    {
        "nombre": "Plancha lateral",
        "tipo_ejercicio": tipos_ejercicio["Resistencia"],
        "grupos": ["Core"],
        "descripcion": "Mantén el cuerpo recto apoyado en un antebrazo de lado.",
    },
    {
        "nombre": "Estiramiento de pectoral en pared",
        "tipo_ejercicio": tipos_ejercicio["Movilidad"],
        "grupos": ["Pecho"],
        "descripcion": "Gira el torso alejándolo del brazo apoyado para abrir el pecho.",
    },
    {
        "nombre": "Curl martillo",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Bíceps"],
        "descripcion": "Flexiona los codos con agarre neutro para trabajar braquial y braquiorradial.",
    },
    {
        "nombre": "Press de hombros en máquina",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Hombros"],
        "descripcion": "Empuja las asas hacia arriba manteniendo el torso estable.",
    },
    {
        "nombre": "Ab wheel",
        "tipo_ejercicio": tipos_ejercicio["Hipertrofia"],
        "grupos": ["Core"],
        "descripcion": "Rueda hacia adelante manteniendo el core firme y vuelve controlado.",
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