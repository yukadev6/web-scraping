import requests

import bs4

results = requests.get('https://skyridgeoutfitters.com/product/id-rather-be-fishing-womens-t-shirt/')

soup = bs4.BeautifulSoup(results.text,'lxml')

image_info = soup.select('.footer-brand img')

product = image_info[0]

product['src']

image_link = requests.get('https://skyridgeoutfitters.com/wp-content/uploads/2020/07/footer-logo.png')

f = open('/Users/yuka/desktop/coding/projects/webscraping/footer_image.jpg','wb')

f.write(image_link.content)

f.close()