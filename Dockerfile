FROM python:3.12

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor en /app
COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al contenedor en /app
COPY . .

EXPOSE 5000

# Ejecuta la aplicación FastAPI cuando se inicie el contenedor
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
