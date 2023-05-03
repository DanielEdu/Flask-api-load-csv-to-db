# Imagen base
FROM python:3.9

# Directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt al directorio /app
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual al directorio /app en el contenedor
COPY . .

# Exponer el puerto 5000
EXPOSE 5000

# Variables de entorno para la conexión a la base de datos
ENV POSTGRES_USER=<usuario>
ENV POSTGRES_PASSWORD=<contraseña>
ENV POSTGRES_HOST=<host>
ENV POSTGRES_PORT=<puerto>
ENV POSTGRES_DB=<base_de_datos>

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
