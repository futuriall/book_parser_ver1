from parser import parse

if __name__ == '__main__':
    book_url = 'http://loveread.ec/read_book.php?id=7468'
    book_name = 'test_book'
    amount_pages = 294
    parse(book_url, book_name, amount_pages)
