
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://store.musinsa.com/app/product/detail/1390339/0')
soup = BeautifulSoup(response, 'html.parser')

for anchor in soup.select("strong#pageview_1m"):
    print(anchor.get_text())
for ex in soup.select("ul.product_article"):
    print(ex.get_text())
for pricesale in soup.select("span.txt_kor_discount"):
    print(pricesale.get_text())

print(pricesale.text)