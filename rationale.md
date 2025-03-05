# rationale.md

This document explains how we validated that the obtained results (word cloud, figure count, and extracted links) are correct.

## 1. Validation of Abstract Extraction and Word Cloud

1. **Abstract Extraction:**  
   - We use Grobid to parse each PDF and search for the `<abstract>` section in the returned TEI.  
   - For PDFs where no `<abstract>` is detected, we take the first paragraph from `<body>` as a fallback.  
   - We manually compared the extracted text with the actual abstract from two PDFs (e.g., `2502.13007v1.pdf` and `2502.14358v1.pdf`). The extracted text largely matched the actual abstract.

2. **Word Cloud:**  
   - We checked whether the most frequent words correspond to the main topics of the articles (e.g., "FRS codes", "decoding", "multiplicity").  
   - We ensured that only meaningful words appeared and filtered out namespace elements or URLs.

## 2. Validation of Figure Count

- Grobid tags `<figure>` elements in the TEI. We increment the counter for each `<figure>` found.  
- We manually reviewed two PDFs and counted the figures to verify that the number matched the generated output.  
- Example: `2502.14358v1.pdf` contains three figures identified as `<figure>` in the TEI; in the PDF, we verified three corresponding "Figure…" sections.

## 3. Validation of Extracted Links

- We use a regular expression (`https?://...`) to capture URLs from the TEI.  
- We inspected the `*links.txt` file of a specific PDF, confirming that the extracted URLs correspond to bibliographic references or cited websites within the PDF.  
- Since Grobid sometimes returns namespaces, we manually filtered out URLs that do not add value (e.g., `http://www.tei-c.org/ns/1.0`).

## 4. Conclusions

Through this manual review of multiple PDFs, we confirmed that:
- The extracted abstracts are accurate (or reasonable).
- The figure count is correct in the tested cases.
- The listed links match those found in the PDF.

Therefore, we consider the solution to be reliable.

---

# 📌 Sección en Español

Este documento explica cómo validamos que los resultados obtenidos (nube de palabras, recuento de figuras y enlaces) son correctos.

## 1. Validación del abstract y la nube de palabras

1. **Extracción del abstract:**  
   - Usamos Grobid para parsear cada PDF y buscamos la sección `<abstract>` en el TEI devuelto.  
   - Para PDFs en los que no se detecta un `<abstract>`, tomamos el primer párrafo de `<body>` (fallback).  
   - Comparamos manualmente en 2 PDFs (por ejemplo, `2502.13007v1.pdf` y `2502.14358v1.pdf`) el texto extraído versus el abstract real del PDF. Coincidían en gran medida.

2. **Nube de palabras:**  
   - Revisamos si las palabras frecuentes se corresponden a los temas centrales de los artículos (p. ej., "FRS codes", "decoding", "multiplicity").  
   - Verificamos que no aparecieran únicamente palabras de namespace o URLs (filtramos un poco).

## 2. Validación del recuento de figuras

- Grobid etiqueta `<figure>` en el TEI. Por cada `<figure>`, incrementamos el contador.  
- Abrimos manualmente 2 PDFs y contamos las figuras para confirmar que el número coincide con la salida.  
- Ejemplo: `2502.14358v1.pdf` contiene 3 figuras identificadas como `<figure>` en el TEI; en el PDF se ven 3 secciones “Figure…”.

## 3. Validación de enlaces

- Usamos una expresión regular (`https?://...`) para capturar URLs del TEI.  
- Inspeccionamos el archivo `*links.txt` de un PDF concreto, confirmando que esas URLs corresponden a referencias bibliográficas o sitios mencionados en el PDF.  
- Dado que Grobid a veces retorna namespaces, filtramos manualmente las URLs que no aportan valor (ej.: `http://www.tei-c.org/ns/1.0`).

## 4. Conclusiones

Con esta revisión manual en varios PDFs, confirmamos que:
- Los abstracts extraídos son fieles (o razonables).
- El recuento de figuras es correcto en los casos probados.
- Los enlaces listados coinciden con lo que aparece en el PDF.

Por tanto, consideramos que la solución funciona adecuadamente.