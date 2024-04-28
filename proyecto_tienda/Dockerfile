# Usar una imagen oficial de Python como imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copiar el archivo de requisitos y instalar las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copiar el script de entrypoint y dar permisos de ejecución
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


# Exponer el puerto en el que la aplicación estará disponible
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
