import pdb
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
# print(find_div_2)

Bookstore_info = find_div_2[0].find_all('div', class_='shop-item span6 mobile-span12')
# print(Bookstore_info)

with open('name_address.txt', 'w') as file:
    for each_bookstore in Bookstore_info:
        name_of_bookstore = each_bookstore.find('a', class_='title link-invert')
        address_of_bookstore = each_bookstore.find('a', class_='shop-address')
        # striped_address = address_of_bookstore.text.strip()
        # striped_address = striped_address.replace(' ', '')
        seprated_address = ' '.join(address_of_bookstore.text.split())

        print('Bookstore name: ')
        print(name_of_bookstore.text.strip())

        print('\n')

        print('address_of_bookstore: ')
        print(seprated_address)
        print('\n')
        # print(address_of_bookstore.text.strip())

        file.write('Bookstore name:')
        file.write(name_of_bookstore.text.strip())
        file.write('\n')
        file.write('Bookstore_address: ')
        file.write(seprated_address)
        file.write('\n')
