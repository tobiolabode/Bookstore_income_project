from bs4 import BeautifulSoup
import requests


page = requests.get("https://www.waterstones.com/bookshops/viewall")

soup = BeautifulSoup(page.text, 'html.parser')

main_container_div_element = soup.body.div
first_sibling_div = soup.body.div.div
parent_first_sibling_div = first_sibling_div.parent


find_div = main_container_div_element.find_all('div', class_="main-page row")
print(find_div[0])
# print(soup.body.div.div.next_sibling.prettify())
