import csv
import time
from bs4 import BeautifulSoup
import requests

pages = [str(i) for i in range(1, 15)]  # Creates list of numbers to be used for URL

with open('dataset.csv', 'w') as dataset_file:
    dataset_writer = csv.writer(dataset_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    dataset_writer.writerow(['Bookstore name,  Street_name, Town, Postcode'])

    for each_page in pages:
        page = requests.get("https://www.waterstones.com/bookshops/viewall" + '/page/' + each_page)

        if page.status_code != 200:
            print('REQUEST DID NOT GO THROUGH: PAGE {} '.format(each_page))

        print('Waiting ...')
        time.sleep(10)

        soup = BeautifulSoup(page.text, 'html.parser')

        main_container_div_element = soup.body.div

        find_div = main_container_div_element.find_all('div', class_="main-page row")
        # print(find_div[0])

        find_div_2 = find_div[0].find_all(
            'div', class_='shops-directory-list span12 alpha omega section')
        # print(find_div_2)

        Bookstore_info = find_div_2[0].find_all('div', class_='shop-item span6 mobile-span12')
        # print(Bookstore_info)

        print('\n --------------------------- \n')
        print('Page Number {}'.format(each_page))
        print('\n --------------------------- \n')

        print('Bookstore name, Street_name, Town, Postcode')
        for each_bookstore in Bookstore_info:
            name_of_bookstore = each_bookstore.find('a', class_='title link-invert')
            address_of_bookstore = each_bookstore.find('a', class_='shop-address')
            seprated_address = ' '.join(address_of_bookstore.text.split())

            print(name_of_bookstore.text.strip(), seprated_address)

            print('\n')

            dataset_writer.writerow([name_of_bookstore.text.strip(), seprated_address])
