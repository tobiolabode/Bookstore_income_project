from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

df = pd.read_csv('filtered_dataset.csv')
list_postcodes = list(df['Postcode'])

# print(list_postcodes)

names_boroughs = []

url = 'https://www.gov.uk/find-local-council'

driver = webdriver.Firefox()

i = 0

for postcode in list_postcodes:

    print('Bookstore: {}'.format(df['Bookstore name'].iloc[i]))
    i += 1

    driver.implicitly_wait(20)
    print('Waiting ...')
    driver.get(url)

    inputElement = driver.find_element_by_id('postcode')
    inputElement = inputElement.send_keys(postcode)

    find_button = driver.find_element_by_xpath(
        '/html/body/div[6]/div[1]/main/div/form/fieldset/div/button')
    find_button.click()

    soup = BeautifulSoup(driver.page_source, 'lxml')
    result_layer = soup.find('div', class_='unitary-result group')
    name_borough = result_layer.p.text

    print(name_borough)
    names_boroughs.append(name_borough)

    print('Waiting ...')
    time.sleep(10)

    # driver.execute_script("window.history.go(-1)")


driver.quit()

df['Borough'] = names_boroughs

print(df.head())

df.to_csv('filtered_dataset_boroughs.csv', index=False)
