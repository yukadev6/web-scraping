import requests

import bs4

base_url = 'http://quotes.toscrape.com/page/{}/'
page_still_valid = True
authors = set()
page=1

while page_still_valid:
    page_url = base_url.format(page)
    result = requests.get(page_url)
    
    if "No quotes found!" in result.text:
        break
    
    soup = bs4.BeautifulSoup(result.text,'lxml')
   
    for name in soup.select('.author'):
        authors.add(name.text)
        
    page = page+1

print(sorted(authors))