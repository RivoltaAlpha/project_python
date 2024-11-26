import requests
from bs4 import BeautifulSoup

def fetch_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2')
    for title in titles:
        print(title.get_text())

url = "http://mwanikitiff.me/Recipe_css/"
fetch_titles(url)
