import requests

import bs4

results = requests.get("https://yukasrecipes.com/carrot-cake-with-whipped-cream-cheese-frosting/")

soup = bs4.BeautifulSoup(results.text,'lxml')

image_info = soup.select('.attachment-firefly-coding-featured-image')

logo = image_info[0]

logo['src']

image_link = requests.get('https://yukasrecipes.com/wp-content/uploads/2020/06/carrot-cake.jpg')

f = open('/Users/yuka/desktop/coding/projects/webscraping/cake_image.jpg','wb')

f.write(image_link.content)

f.close()