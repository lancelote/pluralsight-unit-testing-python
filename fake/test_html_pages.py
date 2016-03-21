# coding=utf-8

""""HTML Converter"""

import io
import os
import tempfile
import unittest

from .html_pages import HtmlPagesConverter, FileAccessWrapper


class HtmlPagesTest(unittest.TestCase):

    def test_inserts_br_tags_for_linebreaks(self):
        filename = os.path.join(tempfile.gettempdir(), 'file.txt')
        f = open(filename, 'w', encoding='UTF-8')
        f.write('plain text\n')
        f.close()
        converter = HtmlPagesConverter(FileAccessWrapper(filename))
        new_text = converter.get_html_page(0)
        self.assertEqual(new_text, 'plain text<br />')

    def test_quotes_escaped(self):
        converter = HtmlPagesConverter(FakeFileWrapper("text with 'quotes'"))
        new_text = converter.get_html_page(0)
        self.assertEqual(new_text, 'text with &#x27;quotes&#x27;<br />')

    def test_random_access_pages(self):
        text = 'Page one\nPAGE_BREAK\npage two\nPAGE_BREAK\n'
        converter = HtmlPagesConverter(FakeFileWrapper(text))
        page_two = converter.get_html_page(1)
        self.assertEqual('page two<br />', page_two)

    def test_nonexistent_file(self):
        converter = HtmlPagesConverter(FileAccessWrapper('missing'))
        self.assertEqual('', converter.get_html_page(0))


class FakeFileWrapper(object):

    def __init__(self, text):
        self.text = text

    def open(self):
        return io.StringIO(self.text)
