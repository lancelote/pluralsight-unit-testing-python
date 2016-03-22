# coding=utf-8

""""HTML Converter"""


import html as html_converter


class FileAccessWrapper(object):

    def __init__(self, filename):
        self.filename = filename

    def open(self):
        return open(self.filename, 'r', encoding='UTF-8')


class HtmlPagesConverter(object):

    def __init__(self, file_access):
        """Read the file and note the position of the page breaks so we can
        access them

        Args:
            file_access: FileAccessWrapper
        """
        self.file_access = file_access
        self.breaks = [0]

        try:
            with self.file_access.open() as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    line = line.rstrip()
                    if 'PAGE_BREAK' in line:
                        page_break_position = f.tell()
                        self.breaks.append(page_break_position)
                self.breaks.append(f.tell())
        except FileNotFoundError:
            pass

    def get_html_page(self, page):
        """Return html page with the given number (zero indexed)

        Args:
            page (int): Number of html page

        Returns:
            str: html code
        """
        if self.breaks == [0]:
            return ''

        page_start = self.breaks[page]
        page_end = self.breaks[page + 1]
        html = ''

        with self.file_access.open() as f:
            f.seek(page_start)
            while f.tell() != page_end:
                line = f.readline()
                line = line.rstrip()
                if 'PAGE_BREAK' in line:
                    continue
                html += html_converter.escape(line, quote=True)
                html += '<br />'
        return html
