# AI Open Science Text Analysis

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

## Instalación y uso

### 1. Clonar este repositorio:

```bash
git clone https://github.com/sergarsilla/ai-open-science-text-analysis.git
cd ai-open-science-text-analysis
```

### 2. Ejecutar la aplicación con Docker Compose (recomendado)

Este método permite ejecutar todo el sistema en un solo paso, sin necesidad de instalar dependencias manualmente.

1. **Instalar Docker Compose:** Si aún no lo tienes instalado, sigue las instrucciones oficiales de [Docker Compose](https://docs.docker.com/compose/install/).

2. **Ejecutar la aplicación:**

   ```bash
   docker compose up --build
   ```

   Esto construirá la imagen, iniciará Grobid y ejecutará el análisis automáticamente sobre los PDFs en la carpeta `papers/`.

3. **Resultados:**

   Una vez finalizada la ejecución, los resultados estarán en la carpeta `output/`:

   - `wordcloud.png`: Nube de palabras basada en los resúmenes de los artículos.
   - `figures_per_article.png`: Gráfico de barras con el número de figuras por artículo.
   - `urls_per_article.txt`: Listado de enlaces extraídos de cada artículo.

4. **Detener la aplicación:**

   Para detener y limpiar los servicios de Docker Compose, usa:

   ```bash
   docker compose down
   ```

### 3. Alternativa: Ejecutar manualmente sin Docker Compose

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
├── papers/                  # PDFs de ejemplo a analizar
├── output/                  # Salidas generadas (nube, enlaces, etc.)
├── scripts/                 # Script principal (analyze.py) y otros
├── requirements.txt         # Dependencias Python
├── Dockerfile               # (Opcional) para contenerizar tu propia imagen
├── README.md                # Este archivo de documentación
├── rationale.md             # Documento explicando la validación de resultados
├── CITATION.cff             # Cómo citar este repositorio (opcional)
├── LICENSE                  # Licencia (MIT, Apache, etc.)
└── .gitignore               # Ignora venv, __pycache__, etc.
```

## Licencia

Este proyecto se distribuye bajo la licencia **Apache** (o la que prefieras).
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
Si te resulta útil, no olvides dejar una estrella en GitHub o mencionarlo en tus trabajos.
