from bs4 import BeautifulSoup
import requests
yt_text=requests.get("https://www.olx.com.pk/").text
soup=BeautifulSoup(yt_text,'lxml')
item=soup.find('div',class_="_948d9e0a _7c843346 _95d4067f e1c7c3d4 _4122130d")#_948d9e0a _7c843346 _95d4067f e1c7c3d4 _4122130d
categoray=item.find_all('div',class_="e778ee91")
for categ in categoray:
    name=categ.find('span',class_='_5d20b0c4')
    print(name.text)





