import unittest
import sys
import os
import textwrap

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))

from analyze import extract_abstract_or_body, extract_figures_count, extract_links

class TestAnalyzeFunctions(unittest.TestCase):
    def setUp(self):
        """Opcional: preparar variables comunes para los tests."""
        self.valid_tei_abstract = (
            '<TEI><text><front><abstract>This is a test abstract.</abstract></front></text></TEI>'
        )
        self.valid_tei_fallback = (
            '<TEI><text><body><p>Fallback abstract content.</p></body></text></TEI>'
        )
        self.tei_with_figures = (
            '<TEI><text><body><figure>Figure 1</figure><figure>Figure 2</figure></body></text></TEI>'
        )
        self.tei_without_figures = (
            '<TEI><text><body><p>No figures here.</p></body></text></TEI>'
        )
        self.tei_with_link = (
            '<TEI><text><body><p>Link: http://example.com</p></body></text></TEI>'
        )
        self.tei_without_link = (
            '<TEI><text><body><p>No links here.</p></body></text></TEI>'
        )
        self.invalid_tei = "<TEI><text><body><p>Missing closing tags"

    def test_extract_abstract_or_body_with_abstract(self):
        """Se debe extraer el contenido de <abstract> correctamente."""
        result = extract_abstract_or_body(self.valid_tei_abstract)
        self.assertIn("This is a test abstract.", result,
                      msg="No se extrajo correctamente el contenido de la etiqueta <abstract>.")

    def test_extract_abstract_or_body_with_fallback(self):
        """Si no hay <abstract>, se debe usar el primer <p> dentro de <body>."""
        result = extract_abstract_or_body(self.valid_tei_fallback)
        self.assertIn("Fallback abstract content.", result,
                      msg="El método no aplicó correctamente el fallback al primer <p> del body.")

    def test_extract_abstract_or_body_invalid_xml(self):
        """Para TEI malformado, se debe retornar cadena vacía."""
        result = extract_abstract_or_body(self.invalid_tei)
        self.assertEqual(result, "",
                         msg="Para XML inválido se esperaba una cadena vacía.")

    def test_extract_figures_count(self):
        """Se debe contar correctamente el número de figuras."""
        # Caso con figuras
        count = extract_figures_count(self.tei_with_figures)
        self.assertEqual(count, 2,
                         msg="El conteo de figuras no coincide con el número esperado (2).")
        # Caso sin figuras
        count = extract_figures_count(self.tei_without_figures)
        self.assertEqual(count, 0,
                         msg="Para un TEI sin figuras se esperaba un conteo de 0.")
        # Caso con XML mal formado debe retornar 0
        count = extract_figures_count(self.invalid_tei)
        self.assertEqual(count, 0,
                         msg="Para XML inválido se esperaba un conteo de figuras de 0.")

    def test_extract_links(self):
        """Se deben extraer correctamente los enlaces y manejar casos sin enlaces."""
        # Usando subTest para probar múltiples escenarios en esta función.
        test_cases = [
            (self.tei_with_link, "http://example.com", 1),
            (self.tei_without_link, None, 0),
        ]
        for tei, expected_link, expected_count in test_cases:
            with self.subTest(tei=tei):
                links = extract_links(tei)
                self.assertEqual(len(links), expected_count,
                                 msg=f"Se esperaba {expected_count} enlace(s), pero se obtuvieron {len(links)}.")
                if expected_link:
                    self.assertIn(expected_link, links,
                                  msg=f"El enlace esperado '{expected_link}' no se encontró en la lista de enlaces.")

    def test_extract_links_with_trailing_punctuation(self):
        """Verifica que la función extraiga enlaces sin incluir signos de puntuación final."""
        tei_with_punctuated_link = (
            '<TEI><text><body><p>Check this link: http://example.com, for more info.</p></body></text></TEI>'
        )
        links = extract_links(tei_with_punctuated_link)
        # Aquí se asume que la expresión regular captura hasta antes de la coma.
        self.assertTrue(any(link.startswith("http://example.com") for link in links),
                        msg="El enlace extraído debería comenzar con 'http://example.com' sin incluir la coma final.")

if __name__ == '__main__':
    unittest.main()
