from bs4 import BeautifulSoup
import requests
btc_html=requests.get("https://www.google.com/finance/quote/BTC-USD?sa=X&ved=2ahUKEwjv8cm0o5WRAxU7T0EAHfm0KUcQ-fUHegQIDRAd").text
soup=BeautifulSoup(btc_html,"lxml")
# print(soup)
pc=soup.find('div',attrs={'data-source': 'BTC', 'data-target': 'USD'})
price=pc.find('div',class_="YMlKec fxKbKc").text
print(price)
