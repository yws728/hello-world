from libs.stringGetter import getPageString
from bs4 import BeautifulSoup

def getProducts(string):
    bsObj = BeautifulSoup(string, "html.parser")
    ul = bsObj.find("ul", {"id": "searchList"})
    lis = ul.findAll("li", {"class": "li_box"})
    li = lis[0]

    print(li)

    return[]


url = "https://store.musinsa.com/app/items/lists/001/?category=&d_cat_cd=001&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=90&page=1&page_kind=category&list_kind=small&free_dlv=&ex_soldout=&sale_goods=&exclusive_yn=&price=&color=&a_cat_cd=&sex=&size=&tag=&popup=&brand_favorite_yn=&goods_favorite_yn=&blf_yn=&campaign_yn=&price1=&price2=&brand_favorite=&goods_favorite=&chk_exclusive=&chk_sale=&chk_soldout="
pageString = getPageString(url)
print(getProducts(pageString))