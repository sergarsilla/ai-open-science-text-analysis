# rationale.md

Este documento explica cómo validamos que los resultados obtenidos (nube de palabras, recuento de figuras y enlaces) son correctos.

## 1. Validación del abstract y la nube de palabras

1. **Extracción del abstract:**  
   - Usamos Grobid para parsear cada PDF y buscamos la sección `<abstract>` en el TEI devuelto.  
   - Para PDFs en los que no se detecta un `<abstract>`, tomamos el primer párrafo de `<body>` (fallback).  
   - Comparamos manualmente en 2 PDFs (por ejemplo, `2502.13007v1.pdf` y `2502.14358v1.pdf`) el texto extraído versus el abstract real del PDF. Coincidían en gran medida.

2. **Nube de palabras:**  
   - Revisamos si las palabras frecuentes se corresponden a los temas centrales de los artículos (p. ej., “FRS codes”, “decoding”, “multiplicity”).  
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
