from bs4 import BeautifulSoup
import requests

Game = "sonicfrontiers"

html = requests.get("https://isthereanydeal.com/game/" + Game + "/info/")
soup = BeautifulSoup(html.text, "lxml")

price_panels = soup.find_all("td", class_="priceTable__new")
print(type(price_panels))
prices = [panel.text.strip() for panel in price_panels]

# remove duplicate values in prices list
prices= set(prices)

for price in prices:
    print(price)

