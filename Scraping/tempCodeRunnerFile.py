from bs4 import BeautifulSoup
import requests
yt_text=requests.get("https://www.youtube.com/watch?v=G3e-cpL7ofc&t=1411s").text
soup=BeautifulSoup(yt_text,'lxml')
print(soup.prettify())
