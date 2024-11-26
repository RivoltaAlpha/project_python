import requests
from bs4 import BeautifulSoup

def fetch_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2')
    for title in titles:
        print(title.get_text())

url = "<https://important-jay-07d.notion.site/Python-Crash-Course-35b6532cfa5b4e5a96ef9ff45faaf5b9#5899bc7d96e1425a8708774e34a5fb87>"
fetch_titles(url)
