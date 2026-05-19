# ── Build stage ───────────────────────────────────────────
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# 1. Copiar requirements
COPY requirements.txt .

# 2. Instalar dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# 3. Copiar TODO el proyecto
COPY . .

# 4. Ejecutar collectstatic AHORA que manage.py existe
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "portgas_health.wsgi:application", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "3", \
     "--timeout", "120"]

