from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
print(page)

Soup = bs(page.text,'html.parser')

Stars = Soup.find('table')

tempList= []
tableRows = Stars.find_all('tr')
for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)

StarNames = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(tempList)):
    StarNames.append(tempList[i][1])
    Distance.append(tempList[i][3])
    Mass.append(tempList[i][5])
    Radius.append(tempList[i][6])
    Lum.append(tempList[i][7])
    
DATA = pd.DataFrame(list(zip(StarNames,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(DATA)

DATA.to_csv('Stars.csv')