from unittest import TestCase

from parser import get_page, get_page_book_content


class TestPageParser(TestCase):
    def test_i(self):
        pass


class TestPageDownloader(TestCase):
    def test_get_page(self):
        url = 'http://loveread.ec/read_book.php?id=7468&p=30'
        text = get_page(url)
        self.assertIsNotNone(text)


class TestPageContentExtractor(TestCase):
    def test_get_page_book_content(self):
        html_page = get_file('./assets/test_page.htm')
        content = get_page_book_content(html_page)
        print(content)


def get_file(file_path):
    with open(file_path, 'r', encoding='cp1251') as test_file:
        html_page = ''.join(test_file.readlines())
    return html_page
