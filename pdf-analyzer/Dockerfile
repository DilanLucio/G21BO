# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para PyMuPDF
RUN apt-get update && apt-get install -y build-essential

# Copiar requerimientos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código
COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Comando para iniciar la app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
