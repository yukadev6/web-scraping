import requests

import bs4

results = requests.get("https://skyridgeoutfitters.com/")

soup = bs4.BeautifulSoup(results.text,'lxml')

image_info = soup.select('.custom-logo')

logo = image_info[0]

logo['src']

image_link = requests.get('https://skyridgeoutfitters.com/wp-content/uploads/2020/07/cropped-logo-1-2.png')

f = open('/Users/yuka/desktop/coding/projects/webscraping/logo_image.jpg','wb')

f.write(image_link.content)

f.close()