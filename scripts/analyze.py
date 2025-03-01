import os
import requests
import lxml.etree as ET
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

GROBID_ENDPOINT = "http://localhost:8070/api/processFulltextDocument"
PAPERS_FOLDER = "papers"
OUTPUT_FOLDER = "output"

def process_pdf(file_path):
    """Envía un PDF a Grobid y devuelve el contenido TEI en formato string."""
    with open(file_path, 'rb') as f:
        response = requests.post(
            GROBID_ENDPOINT,
            files={'input': (os.path.basename(file_path), f)},
            data={'consolidateCitations': '0'}  # Cambia a '1' si quieres consolidar citas
        )
    return response.text

def extract_abstract_or_body(tei_content, filename_for_debug=""):
    """
    Extrae un texto "similar a abstract".
    Ignora namespaces usando local-name() para que <abstract> y compañía coincidan aunque
    el TEI declare xmlns="http://www.tei-c.org/ns/1.0".

    Orden de búsqueda:
    1) <abstract>
    2) <div type="abstract">
    3) <p type="abstract">
    4) Fallback: primer <p> dentro de <body>

    Si no encuentra nada, retorna cadena vacía.
    """
    try:
        root = ET.fromstring(tei_content.encode('utf-8'))
    except ET.XMLSyntaxError:
        return ""

    # 1) <abstract>
    abstracts = root.xpath('.//*[local-name()="abstract"]')
    if abstracts:
        return "".join(abstracts[0].itertext()).strip()

    # 2) <div type="abstract">
    div_abstracts = root.xpath('.//*[local-name()="div"][@type="abstract"]')
    if div_abstracts:
        return " ".join("".join(x.itertext()) for x in div_abstracts).strip()

    # 3) <p type="abstract">
    p_abstracts = root.xpath('.//*[local-name()="p"][@type="abstract"]')
    if p_abstracts:
        return " ".join("".join(x.itertext()) for x in p_abstracts).strip()

    # 4) Fallback: primer párrafo en <body>
    #    (ignorando namespace con local-name())
    body_paras = root.xpath('.//*[local-name()="body"]//*[local-name()="p"]')
    if body_paras:
        return "".join(body_paras[0].itertext()).strip()

    return ""

def extract_figures_count(tei_content):
    """Cuenta cuántas <figure> hay en el TEI (ignorando namespaces)."""
    try:
        root = ET.fromstring(tei_content.encode('utf-8'))
    except ET.XMLSyntaxError:
        return 0

    figures = root.xpath('.//*[local-name()="figure"]')
    return len(figures)

def extract_links(tei_content):
    """Busca URLs a partir del TEI (método rápido con regex)."""
    urls = re.findall(r'https?://[^\s<]+', tei_content)
    return urls

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    figures_dict = {}
    all_abstract_words = []

    for filename in os.listdir(PAPERS_FOLDER):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(PAPERS_FOLDER, filename)

            # 1) Extraer TEI usando Grobid
            tei = process_pdf(pdf_path)

            # 2) Extraer texto del "abstract" o fallback
            abstract_text = extract_abstract_or_body(tei, filename_for_debug=filename)

            if not abstract_text.strip():
                # Guardamos TEI en debug si está vacío
                debug_tei_path = os.path.join(OUTPUT_FOLDER, f"debug_tei_{filename}.xml")
                with open(debug_tei_path, 'w', encoding='utf-8') as debug_file:
                    debug_file.write(tei)
                print(f"[WARN] No se encontró abstract ni body en '{filename}'. "
                      f"Se guardó su TEI en '{debug_tei_path}'")
            else:
                # Añadimos las palabras a la lista global
                all_abstract_words.extend(abstract_text.split())

            # 3) Contar figuras
            fig_count = extract_figures_count(tei)
            figures_dict[filename] = fig_count

            # 4) Extraer links y guardarlos
            links = extract_links(tei)
            links_output_path = os.path.join(OUTPUT_FOLDER, f"{filename}_links.txt")
            with open(links_output_path, 'w') as link_file:
                for link in links:
                    link_file.write(f"{link}\n")

    # -- Crear la nube de palabras
    text_for_cloud = " ".join(all_abstract_words)
    if not text_for_cloud.strip():
        print("No se han encontrado palabras para crear la nube. "
              "Revisa los ficheros debug_tei_*.xml en 'output' para ver la estructura TEI.")
    else:
        wc = WordCloud(width=800, height=600, background_color="white").generate(text_for_cloud)
        plt.figure(figsize=(8, 6))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        plt.title("Nube de Palabras (Abstract + Fallback)")
        plt.savefig(os.path.join(OUTPUT_FOLDER, "wordcloud_abstracts.png"))
        plt.close()

    # -- Visualización del número de figuras por artículo
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(figures_dict)), figures_dict.values(), align='center')
    plt.xticks(range(len(figures_dict)), list(figures_dict.keys()), rotation=45, ha='right')
    plt.ylabel("Número de Figuras")
    plt.title("Figuras por Artículo")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "figures_per_article.png"))
    plt.close()

    print("Análisis completado. Revisa la carpeta 'output' para resultados y archivos debug.")

if __name__ == "__main__":
    main()
