from selenium import webdriver
driver = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')

from bs4 import BeautifulSoup

driver.get('https://store.musinsa.com/app/items/lists/001')
html = driver.page_source
for pageNo in range(1, 10+1):
    driver.find_element_by_xpath('//*[@id="searchList"]/li[{}]/div[3]/div[1]/a/img'.format(pageNo)).click()

soup = BeautifulSoup(html, 'html.parser')