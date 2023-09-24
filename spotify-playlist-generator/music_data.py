import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/2010-02-06/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")


print(soup.select_one("#title-of-a-story").text)
print(soup.select_one(".o-chart-results-list__item").text)
# print(soup.find("li").text)