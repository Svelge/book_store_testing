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
driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/product/html5-forms/"]').click()

h1 = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1.product_title.entry-title"), "HTML5 Forms"))

driver.quit()

