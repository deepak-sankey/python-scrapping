import requests
import bs4
import urllib.request
from selenium import webdriver


def scrape():
    driver=webdriver.Chrome("chromedriver.exe")
    driver.get("http://epaper.esakal.com")
    for x in range(12):
        # nbutton=driver.find_element_by_id("lnkNext")
        frm=driver.find_element_by_id("frm")
        frm=frm.get_attribute("innerHTML")
        soup=bs4.BeautifulSoup(frm,"lxml")
        print(soup.FindElementById("bgImage"))	

        return soup.FindElementById("bgImage")
        # for j in soup.find_all("area"):
        #     urllib.request.urlretrieve(soup.find_all("area")[i]..attrs['data-src'],"D:\\Ansari Saad\\"+str(x)+str(i)+".jpg")
        #     i=i+1
        # nbutton.click()