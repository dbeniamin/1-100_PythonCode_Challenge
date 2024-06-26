import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome()
driver.set_window_size(1000, 800)
driver.get(URL)
driver.implicitly_wait(10)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Beniamin")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Drimus")

email_address = driver.find_element(By.NAME, "email")
email_address.send_keys("progress@learning.com")

sign_up = driver.find_element(By.XPATH, "/html/body/form/button")
sign_up.click()


time.sleep(2)
driver.quit()
