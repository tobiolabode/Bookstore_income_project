from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

url = 'https://www.gov.uk/find-local-council'


driver = webdriver.Firefox()
driver.implicitly_wait(15)
print('Waiting ...')
driver.get(url)

inputElement = driver.find_element_by_id('postcode')
inputElement = inputElement.send_keys('TW9 1TN')

find_button = driver.find_element_by_xpath(
    '/html/body/div[6]/div[1]/main/div/form/fieldset/div/button')
find_button.click()

soup = BeautifulSoup(driver.page_source, 'lxml')
result_layer = soup.find('div', class_='unitary-result group')
name_borough = result_layer.p.text

print(name_borough)
