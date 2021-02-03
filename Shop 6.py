import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(6)
driver.get("http://practice.automationtesting.in/")

driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]').click()

driver.execute_script("window.scrollBy(0, 300);")

driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=181"]').click()
time.sleep(3)
driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=165"]').click()

driver.find_element_by_css_selector('.wpmenucart-icon-shopping-cart-0').click()

driver.find_element_by_css_selector('a.remove[data-product_id="181"]').click()
time.sleep(3)
driver.find_element_by_css_selector('div.woocommerce-message>a').click()

driver.find_element_by_css_selector('.quantity>input[name="cart[9766527f2b5d3e95d4a733fcfb77bd7e][qty]"').clear()

quantity = driver.find_element_by_css_selector('.quantity>input[name="cart[9766527f2b5d3e95d4a733fcfb77bd7e][qty]"')
quantity.send_keys('3')

driver.find_element_by_xpath('//input[@value="Update Basket"]').click()

element = driver.find_element_by_css_selector(".quantity>input")
element_check = element.get_attribute('value')
if  element_check == '3':
    print('True')
else:  print('False')

time.sleep(3)

driver.find_element_by_xpath('//input[@name="apply_coupon"]').click()

error_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce>.woocommerce-error>li"), "Please enter a coupon code."))

driver.quit()

