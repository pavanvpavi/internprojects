import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.worldometers.info/world-population/population-by-country/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
rows=soup.find('table',{'id':'example2'}).find('tbody').find_all('tr')
countries_list=[]
for row in rows:
    dic={}
    dic['SL.NO']=row.find_all('td')[0].text
    dic['COUNTRY']=row.find_all('td')[1].text
    dic['POPULATION']=row.find_all('td')[2].text
    dic['YEARLY CHANGE']=row.find_all('td')[3].text
    dic['NET CHANGE']=row.find_all('td')[4].text
    dic['DENSITY(P/Km²)']=row.find_all('td')[5].text
    dic['LAND AREA(Km²)']=row.find_all('td')[6].text
    dic['MIGRANTS(net)']=row.find_all('td')[7].text
    dic['FERT.RATE']=row.find_all('td')[8].text
    dic['MID AGE']=row.find_all('td')[9].text
    dic['URBAN POPULATION %']=row.find_ll('td')[10].text
    dic['WORLD SHARE']=row.find_all('td')[11].text
    countries_list.append(dic)
df=pd.DataFrame(countries_list)
df.to_excel('data.xlsx',index=False)
df.to_csv('data.csv',index=False)
