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

driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/product/android-quick-start-guide/"]').click()

price = driver.find_element_by_css_selector('.price>del>span.woocommerce-Price-amount.amount').text
if  price == '600':
    print("True")
else:  print("False")

disc = driver.find_element_by_css_selector('.price ins>span>span').text
if  disc == '450':
    print("True")
else:  print("False")

img = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.images>a>img'))).click()

pp = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.pp_close'))).click()

driver.quit()



