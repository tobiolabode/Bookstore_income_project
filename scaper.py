from bs4 import BeautifulSoup
import requests


page = requests.get("https://www.waterstones.com/bookshops/viewall")

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.head.body)

# print(soup.prettify())
