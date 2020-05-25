import requests
from bs4 import BeautifulSoup


def parse(url: str, book_name: str, amount_pages: int):
    book_path = f'./{book_name}.txt'
    for page_content in book_parser(url, amount_pages):
        save_book_page(book_path, page_content)


def save_book_page(path: str, page_text: str):
    with open(path, 'a') as book_file:
        book_file.write(page_text)


def book_parser(book_url: str, page_amount: int):
    for page_number in range(1, page_amount):
        print(f'parsing of page: {page_number}')
        page_url = book_url + '&p=' + str(page_number)
        page_text = parse_page(page_url)
        yield page_text


def parse_page(url: str):
    page = get_page(url)
    page_text = get_page_book_content(page)
    return page_text


def get_page(url: str):
    res = requests.get(url)
    html_page = res.content
    return html_page


def get_page_book_content(page_html: str):
    soup = BeautifulSoup(page_html, 'html.parser')
    paragraphs = list(soup.find_all('p'))
    res = get_paragraphs_text(paragraphs)
    return res


def get_paragraphs_text(paragraphs):
    res = []
    for p in paragraphs:
        try:
            if 'MsoNormal' in p['class']:
                res.append(p.text)
        except:
            pass
    return ''.join(res)
