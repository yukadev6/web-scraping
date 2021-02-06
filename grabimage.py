import requests

import bs4

results = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(results.text,'lxml')

computer = soup.select('.thumbimage')[0]

computer['src']

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

f = open('/Users/yuka/desktop/coding/Projects/Webscraping/computer_image.jpg','wb')

f.write(image_link.content)

f.close()