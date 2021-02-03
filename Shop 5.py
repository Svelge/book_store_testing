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

driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=181"]').click()

count = driver.find_element_by_css_selector('span.cartcontents')
count_get = count.text
if count == '1':
    print('Count True')
else:  print('Count False')

amount = driver.find_element_by_xpath('//span[@class="amount"]')
amount_get_text = amount.text
if amount.text == '280.00':
    print('Amount True')
else:  print('Amount False')

time.sleep(3)
driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()

subtotal = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, '//td[@data-title="Subtotal"]'), "280.00"))

total = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, '//td[@data-title="Total"]'), "294.00"))

driver.quit()