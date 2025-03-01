# Usa una imagen base de Python 3.10
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos y luego instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código en el contenedor
COPY . .

# Comando por defecto: ejecuta el script principal
CMD ["python", "scripts/analyze.py"]
