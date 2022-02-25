import requests
from bs4 import BeautifulSoup as bs

urls = ["https://www.amazon.in/FASHIMO-Casual-Sneakers-Womens-VK1-Pink-38/dp/B08R3DC9RL/ref=sr_1_4?crid=21IRCNXDZZ2I&keywords=shoes+for+girls&qid=1643640442&sprefix=shoes%2Caps%2C307&sr=8-4"]

headers ={"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

page = requests.get(urls[0], headers=headers)

soup =bs(page.content, "html.parser")

title= soup.find(id="productTitle").get_text()

price = soup.find_all("span", attrs={"class":"a-offscreen"})[0]
