from bs4 import BeautifulSoup
import requests
unfamiliar_skills=input("Enter the skill you dont want :\n >")
html_text=requests.get("https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation=").text
soup=BeautifulSoup(html_text,'lxml')
jobs=soup.find_all('div',class_="srp-listing clearfix")

for job in jobs:
    publish_date=job.find('span',class_="posting-time").text
    # print(publish_date)
    if '4' in publish_date:
        skills=job.find('div',class_='srp-keyskills').text
        experience=job.find('div',class_="srp-exp").text
        link=job.a['href']
        if unfamiliar_skills not in skills:
            print(f"experience= {experience.strip()};")
            print(f"skills= {skills.strip()}")
            print(f"published on:{publish_date.strip()}")
            print(f"link: {link}")
            print('---------------------------------------------------------------------------------------------------')


