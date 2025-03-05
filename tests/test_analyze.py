import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))
from analyze import extract_abstract_or_body, extract_figures_count, extract_links

class TestAnalyzeFunctions(unittest.TestCase):
    def test_extract_abstract_or_body_with_abstract(self):
        # TEI con etiqueta <abstract>
        tei_with_abstract = '<TEI><text><front><abstract>This is a test abstract.</abstract></front></text></TEI>'
        result = extract_abstract_or_body(tei_with_abstract)
        self.assertIn("This is a test abstract.", result)

    def test_extract_abstract_or_body_with_fallback(self):
        # TEI sin abstract, pero con un párrafo en <body>
        tei_no_abstract = '<TEI><text><body><p>Fallback abstract content.</p></body></text></TEI>'
        result = extract_abstract_or_body(tei_no_abstract)
        self.assertIn("Fallback abstract content.", result)

    def test_extract_figures_count(self):
        # TEI con dos figuras
        tei_with_figures = '<TEI><text><body><figure>Figure 1</figure><figure>Figure 2</figure></body></text></TEI>'
        count = extract_figures_count(tei_with_figures)
        self.assertEqual(count, 2)
        
        # TEI sin figuras
        tei_without_figures = '<TEI><text><body><p>No figures here.</p></body></text></TEI>'
        count = extract_figures_count(tei_without_figures)
        self.assertEqual(count, 0)

    def test_extract_links(self):
        # TEI con un enlace
        tei_with_links = '<TEI><text><body><p>Link: http://example.com</p></body></text></TEI>'
        links = extract_links(tei_with_links)
        self.assertIn("http://example.com", links)
        
        # TEI sin enlaces
        tei_without_links = '<TEI><text><body><p>No links here.</p></body></text></TEI>'
        links = extract_links(tei_without_links)
        self.assertEqual(len(links), 0)

if __name__ == '__main__':
    unittest.main()
