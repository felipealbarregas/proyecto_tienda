#!/bin/bash

# Esperar a que Postgres esté disponible
while ! nc -z db 5432; do
  echo "Esperando a que PostgreSQL inicie..."
  sleep 0.1
done
echo "PostgreSQL iniciado"

# Ejecutar migraciones
echo "Aplicando migraciones..."
python manage.py migrate

# Iniciar Gunicorn
echo "Iniciando Gunicorn..."
exec gunicorn --workers 3 --bind 0.0.0.0:8000 proyecto_tienda.wsgi:application
