from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
start_url="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("C:/Users/ACER/Downloads/chromedriver_win32/chromedriver.exe")
browser.get(start_url)
time.sleep(10)
def scrapTheData():
    headers=["NAME","LIGHT_YEARS_FROM_EARTH","PLANET_MASS","STELLAR_MAGNITUDE","DISCOVERY_DATE"]
    planets_data=[]
    for i in range(0,25):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        allUlTag=soup.find_all("ul",attrs={"class","exoplanet"})
        for eachUl in allUlTag:
            allLiTags=eachUl.find_all("li")
            templist=[]
            for index,eachLi in enumerate(allLiTags):
                if(index==0):
                    templist.append(eachLi.find_all("a")[0].contents[0])
                else:
                    templist.append(eachLi.contents[0])
            planets_data.append(templist)
            browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            
    with open("scrapping.csv","w",newline='') as f:
        csvWriter=csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planets_data)
scrapTheData()
