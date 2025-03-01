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
  - (entre otras si las necesitas)

## Instalación y uso

1. **Clonar este repositorio**:
   ```bash
   git clone https://github.com/sergarsilla/ai-open-science-text-analysis.git
   cd ai-open-science-text-analysis
   ```

2. **(Opcional) Crear un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   De esta forma aislas las dependencias.

3. **Levantar Grobid con Docker**:
   ```bash
   docker pull lfoppiano/grobid:0.7.2
   docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
   ```
   Esto inicia el servicio en `http://localhost:8070`.

4. **Coloca los PDFs** en la carpeta `papers/`

5. **Ejecuta el script principal**:
   ```bash
   python scripts/analyze.py
   ```
   Este script enviará cada PDF a Grobid, extraerá su TEI, y luego:
   - Construirá la nube de palabras a partir del *abstract* (o fallback al cuerpo del texto).
   - Contará cuántas `<figure>` detecta Grobid en el TEI.
   - Buscará todos los enlaces que aparezcan en el TEI.

6. **Revisa la carpeta `output/`**:
   - `wordcloud_abstracts.png`: imagen con la nube de palabras.
   - `figures_per_article.png`: gráfica de barras con el recuento de figuras por PDF.
   - `*_links.txt`: ficheros con todos los enlaces detectados en cada PDF.

## Estructura del repositorio

```
ai-open-science-assessment1/
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

Este proyecto se distribuye bajo la licencia **MIT** (o la que prefieras).
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

