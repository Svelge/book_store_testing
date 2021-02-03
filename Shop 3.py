import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(6)
driver.get("http://practice.automationtesting.in/")

driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/my-account/"]').click()

mail = driver.find_element_by_id("username")
mail.send_keys("desirehdman@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("Drkmb5c")

driver.find_element_by_xpath('//input[@value ="Login"]').click()
driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]').click()

selection_one = driver.find_element_by_xpath('//option[@value="price-desc"]')
selection_check_one = selection_one.get_attribute("selected")
assert selection_check_one is None

driver.find_element_by_css_selector("select.orderby").click()
driver.find_element_by_xpath('//option[@value="price-desc"]').click()

selection_two = driver.find_element_by_xpath('//option[@value="price-desc"]')
selection_check_two = selection_two.get_attribute("selected")
assert selection_check_two is not None

driver.quit()

