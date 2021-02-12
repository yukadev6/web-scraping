import requests

import bs4

results = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(results.text,'lxml')

image_info = soup.select('.thumbimage')

kasp = image_info[0]

kasp['src'] 

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')

f = open('/Users/yuka/desktop/coding/Projects/Webscraping/kasp_image.jpg','wb')

f.write(image_link.content)

f.close()