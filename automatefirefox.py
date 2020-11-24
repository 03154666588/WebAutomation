from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

USERNAME = 'moin'
PASSWORD = "12345678"
driver = webdriver.Firefox()
driver.get('http://ps19cms.powersoft19.com/user')
user_input = driver.find_element_by_xpath('//*[@id="edit-name"]')
user_input.send_keys(USERNAME)
password_input = driver.find_element_by_xpath('//*[@id="edit-pass"]')
password_input.send_keys(PASSWORD)
login_button = driver.find_element_by_xpath('//*[@id="edit-submit"]')
login_button.click()

driver.close()
