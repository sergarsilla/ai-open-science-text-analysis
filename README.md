# AI Open Science Text Analysis

This project analyzes open-access PDF articles using [Grobid](https://github.com/kermitt2/grobid) to extract information and generate:
- A **keyword cloud** based on the abstracts of these PDFs.
- A **visualization** (bar chart) showing the **number of figures** per article.
- A **list of links (URLs)** found in each article.

## Requirements

- **Python 3.9+** or later.
- [**Docker**](https://docs.docker.com/) to easily run Grobid.  
  *(Alternatively, if you have Grobid installed differently, adjust the configuration accordingly.)*
- Python libraries (see [`requirements.txt`](./requirements.txt)):
  - `requests`
  - `lxml`
  - `wordcloud`
  - `matplotlib`
  - `...`

## Installation and Usage

### 1. Clone this repository:

```bash
git clone https://github.com/sergarsilla/ai-open-science-text-analysis.git
cd ai-open-science-text-analysis
```

### 2. Create the `papers/` directory and place the PDFs you want to analyze inside

### 3. Create the `output/` directory

### 4. Run the application with Docker Compose (recommended)

This method allows running the entire system in a single step without manually installing dependencies.

1. **Install Docker Compose:** If you haven't installed it yet, follow the official [Docker Compose](https://docs.docker.com/compose/install/) instructions.

2. **Run the application:**

   ```bash
   docker compose up --build
   ```

   This will build the image, start Grobid, and automatically analyze the PDFs in the `papers/` folder.

3. **Results:**

   Once the execution is complete, results will be available in the `output/` directory:

   - `wordcloud_abstracts.png`: Word cloud based on the article abstracts.
   - `figures_per_article.png`: Bar chart showing the number of figures per article.
   - `article_links.txt`: List of links extracted from each article.

4. **Stop the application:**

   To stop and clean up Docker Compose services, use:

   ```bash
   docker compose down
   ```

### 5. Alternative: Run manually without Docker Compose

If you prefer not to use Docker Compose, you can manually run Grobid and the analysis.

#### A. Install dependencies manually

1. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

#### B. Start Grobid manually

If you choose not to use Docker Compose, you can manually run Grobid with Docker:

```bash
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

#### C. Run the analysis manually

```bash
python scripts/analyze.py
```

The PDFs must be placed in the `papers/` folder before running the analysis.

## Repository Structure

```
ai-open-science-text-analysis/
├── papers/                  # PDFs to analyze
├── output/                  # Generated outputs (word cloud, links, etc.)
├── scripts/                 # Main script (analyze.py) and others
├── requirements.txt         # Python dependencies
├── Dockerfile               # (Optional) Containerizing your custom image
├── README.md                # This documentation file
├── rationale.md             # Document explaining result validation
├── CITATION.cff             # How to cite this repository (optional)
├── LICENSE                  # License file
└── .gitignore               # Ignores venv, __pycache__, etc.
```

## License

This project is distributed under the **Apache** license.  
Check the [`LICENSE`](./LICENSE) file for more details.

## How to Cite this Repository

If you want to cite this work, check [`CITATION.cff`](./CITATION.cff).  
GitHub will display a "Cite this repository" box when it detects a `CITATION.cff` file.

## Contact

- Author: **Sergio García Mansilla** (sergarsilla@gmail.com)
- Universidad Politécnica de Madrid (UPM)
- For any suggestions, issues, or questions, open an issue or pull request on GitHub.

---

# 📌 Sección en Español

Este proyecto analiza artículos PDF de acceso abierto usando [Grobid](https://github.com/kermitt2/grobid) para extraer información y generar:
- Una **nube de palabras** (keyword cloud) a partir de los *abstracts* de dichos PDFs.
- Una **visualización** (gráfico de barras) con el **número de figuras** por artículo.
- Un **listado de enlaces (URLs)** encontrados en cada artículo.

## Requisitos

- **Python 3.9+** o superior.
- [**Docker**](https://docs.docker.com/) para levantar Grobid fácilmente.
  *(Alternativamente, si tienes Grobid instalado de otra manera, adapta la configuración.)*
- Librerías Python (ver [`requirements.txt`](./requirements.txt)):
  - `requests`
  - `lxml`
  - `wordcloud`
  - `matplotlib`
  - `...`

## Instalación y uso

### 1. Clonar este repositorio:

```bash
git clone https://github.com/sergarsilla/ai-open-science-text-analysis.git
cd ai-open-science-text-analysis
```

### 2. Crear el directorio `papers/` y colocar los artículos PDF que deseas analizar dentro

### 3. Crear el directorio `output/`

### 4. Ejecutar la aplicación con Docker Compose (recomendado)

Este método permite ejecutar todo el sistema en un solo paso, sin necesidad de instalar dependencias manualmente.

1. **Instalar Docker Compose:** Si aún no lo tienes instalado, sigue las instrucciones oficiales de [Docker Compose](https://docs.docker.com/compose/install/).

2. **Ejecutar la aplicación:**

   ```bash
   docker compose up --build
   ```

   Esto construirá la imagen, iniciará Grobid y ejecutará el análisis automáticamente sobre los PDFs en la carpeta `papers/`.

3. **Resultados:**

   Una vez finalizada la ejecución, los resultados estarán en la carpeta `output/`:

   - `wordcloud_abstracts.png`: Nube de palabras basada en los resúmenes de los artículos.
   - `figures_per_article.png`: Gráfico de barras con el número de figuras por artículo.
   - `article_links.txt`: Listado de enlaces extraídos de cada artículo.

4. **Detener la aplicación:**

   Para detener y limpiar los servicios de Docker Compose, usa:

   ```bash
   docker compose down
   ```

### 5. Alternativa: Ejecutar manualmente sin Docker Compose

Si prefieres no usar Docker Compose, puedes ejecutar Grobid y el análisis manualmente.

#### A. Instalar dependencias manualmente

1. **Crear un entorno virtual (opcional pero recomendado):**

   ```bash
   python3 -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

2. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

#### B. Iniciar Grobid manualmente

Si decides no usar Docker Compose, puedes ejecutar Grobid manualmente con Docker:

```bash
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

#### C. Ejecutar el análisis manualmente

```bash
python scripts/analyze.py
```

Los PDFs deben colocarse en la carpeta `papers/` antes de ejecutar el análisis.

## Estructura del repositorio

```
ai-open-science-text-analysis/
├── papers/                  # PDFs a analizar
├── output/                  # Salidas generadas (nube, enlaces, etc.)
├── scripts/                 # Script principal (analyze.py) y otros
├── requirements.txt         # Dependencias Python
├── Dockerfile               # (Opcional) para contenerizar tu propia imagen
├── README.md                # Este archivo de documentación
├── rationale.md             # Documento explicando la validación de resultados
├── CITATION.cff             # Cómo citar este repositorio (opcional)
├── LICENSE                  # Licencia
└── .gitignore               # Ignora venv, __pycache__, etc.
```

## Licencia

Este proyecto se distribuye bajo la licencia **Apache**.
Revisa el archivo [`LICENSE`](./LICENSE) para más detalles.

## Cómo citar este repositorio

Si quieres citar este trabajo, revisa [`CITATION.cff`](./CITATION.cff).
GitHub mostrará un recuadro de “Cite this repository” cuando detecte un `CITATION.cff`.

## Contacto

- Autor: **Sergio García Mansilla** (sergarsilla@gmail.com)
- Universidad Politécnica de Madrid (UPM)
- Cualquier sugerencia, error o pregunta, envíame un issue/pull request en GitHub.

---
**¡Gracias por usar este proyecto!**
Si te resulta útil, no olvides dejar una estrella en GitHub y/o mencionarlo en tus trabajos.
