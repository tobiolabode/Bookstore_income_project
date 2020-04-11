from bs4 import BeautifulSoup
import requests


page = requests.get("https://www.waterstones.com/bookshops/viewall")

soup = BeautifulSoup(page.text, 'html.parser')

main_container_div_element = soup.body.div
first_sibling_div = soup.body.div.div
parent_first_sibling_div = first_sibling_div.parent


find_div = main_container_div_element.find_all('div', class_="main-page row")
# print(find_div[0])

find_div_2 = find_div[0].find_all('div', class_='shops-directory-list span12 alpha omega section')
print(find_div_2)

Bookstore_info = find_div_2[0].find_all('div', class_='shop-item span6 mobile-span12')
print(Bookstore_info)
