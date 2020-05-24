from selenium import webdriver
driver = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')

from bs4 import BeautifulSoup

driver.get('https://store.musinsa.com/app/items/lists/001')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

pd_name =soup.find('ul', {'id' : 'searchList'}).find_all('p', {'class': 'item_title'})

for name in pd_name:
    print(name.text)
