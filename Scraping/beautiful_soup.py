from bs4 import BeautifulSoup
import os
os.chdir("Scraping")
print(f"you are in ==>{os.getcwd()} ")
with open('index.html','r') as html_file:
    content=html_file.read()

    soup=BeautifulSoup(content,'lxml')
    nav=soup.find_all("div",class_='nav-buttons')
    for name in nav:
        for a in name.find_all('a'):
            print(a.text)
