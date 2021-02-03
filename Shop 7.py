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
driver.find_element_by_css_selector('.wpmenucart-icon-shopping-cart-0').click()

checkout_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.wc-proceed-to-checkout>a"))).click()

nm = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "billing_first_name")))

name = driver.find_element_by_id('billing_first_name')
name.send_keys('John')

surname = driver.find_element_by_id('billing_last_name')
surname.send_keys('Cage')

mail = driver.find_element_by_id('billing_email')
mail.send_keys('desirehdman@gmail.com')

time.sleep(2)
phone = driver.find_element_by_css_selector('input.input-text[name="billing_phone"]')
phone.send_keys('88005553535')

driver.find_element_by_id('s2id_billing_country').click()
country = driver.find_element_by_id('s2id_autogen1_search')
country.send_keys('Qatar')
driver.find_element_by_css_selector('div.select2-result-label').click()

address = driver.find_element_by_id('billing_address_1')
address.send_keys('Pushkina st.')

address2 = driver.find_element_by_id('billing_address_2')
address2.send_keys('2')

city = driver.find_element_by_id('billing_city')
city.send_keys('Zubarah')

state = driver.find_element_by_id('billing_state')
state.send_keys('Mesaid')

zip = driver.find_element_by_id('billing_postcode')
zip.send_keys('1789341')
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
driver.find_element_by_id('payment_method_cheque').click()

driver.find_element_by_id('place_order').click()

ty_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.woocommerce>p"), "Thank you. Your order has been received."))

payment_check = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, "//tfoot/tr[3]/td"), "Check Payments"))

driver.quit()





