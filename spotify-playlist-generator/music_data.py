import requests
from bs4 import BeautifulSoup

base_url = "https://www.billboard.com/charts/hot-100/"

def get_data(date):
    response = requests.get(url=base_url + date)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select(selector="div ul li ul li h3")

    music_titles = []
    for title in result:
        music_titles.append(title.string.strip())

    return music_titles