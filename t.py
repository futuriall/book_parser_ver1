import requests

url = 'http://loveread.ec/read_book.php?id=7468&p=30' #insert a link here
res = requests.get(url)
html_page = res.content


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_page, 'html.parser')

text = soup.find_all(text=True)

set([t.parent.name for t in text])
output = ''
blacklist = [
 '[document]',
 'noscript',
 'header',
 'html',
 'meta',
 'head',
 'input',
 'script',
 # there may be more elements you don't want, such as "style", etc.
]

for t in text:
 if t.parent.name not in blacklist:
  output += '{} '.format(t)
ennd = len(output) - 750
print(output[1630: ennd])
