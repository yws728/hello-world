import requests
from bs4 import BeautifulSoup

def get_bs_obj():
    url = "https://store.musinsa.com/app/product/detail/1390339/0"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

bs_obj = get_bs_obj()

prsale = bs_obj.find("span", {"class": "txt_kor_discount"})
print(prsale.text)

brand = bs_obj.find("strong")
print(brand)