# Usar una imagen oficial de Python como imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    netcat-openbsd \  
    && apt-get clean \  
    && rm -rf /var/lib/apt/lists/* 

# Copiar el archivo de requisitos y instalar las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script de entrypoint y dar permisos de ejecución
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

# Exponer el puerto en el que la aplicación estará disponible
EXPOSE 8000

# Configurar el comando por defecto o el entrypoint
CMD ["./entrypoint.sh"]

