years = list(range(1991,2022)) # defining the years we want to scrape data for

url_start = "https://www.basketball-reference.com/awards/awards_{}.html"

import requests

for year in years:
    url = url_start.format(year)
    data = requests.get(url)
    print(url)
    with open("mvp/{}.html".format(year), "w+", encoding="utf-8") as f:
        f.write(data.text)

from bs4 import BeautifulSoup
with open("mvp/1991.html", encoding="utf-8") as f:
    page = f.read()
soup = BeautifulSoup(page, "html.parser")
over_header1= soup.find('tr', class_="over_header")
if over_header1:  # Check if the element exists
    over_header1.decompose()
mvp_table = soup.find(id="mvp")

import pandas as pd
mvp_1991 = pd.read_html(str(mvp_table))[0]
mvp_1991
mvp_1991.head(1)
mvp_1991["Year"] = 1991
mvp_1991.head()

dfs = []

for year in years:
    with open("mvp/{}.html".format(year)) as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    
    over_header = soup.find('tr', class_="over_header")  # Find the element with class "over_header"
    if over_header:  # Check if the element exists
        over_header.decompose()  # Call decompose() only if the element is found
    
    mvp_table = soup.find(id="mvp")
    mvp_data = pd.read_html(str(mvp_table))[0]
    
    mvp_data["Year"] = year  # Add the "Year" column to the DataFrame
    dfs.append(mvp_data)
