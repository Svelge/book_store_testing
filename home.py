import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(6)
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")

driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/product/selenium-ruby/']").click()
driver.find_element_by_xpath("//a[@href='#tab-reviews']").click()
driver.find_element_by_css_selector(".star-5").click()

comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")

name = driver.find_element_by_id("author")
name.send_keys("Alex")

mail = driver.find_element_by_id("email")
mail.send_keys("desirehdman@gmail.com")

driver.find_element_by_id("submit").click()

time.sleep(3)

driver.quit()