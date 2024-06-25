from selenium import webdriver
from selenium.webdriver.common.by import By

# Amazon captcha solver is required to bypass amazon so chose another site to test on
driver = webdriver.Chrome()
driver.get("https://www.emag.ro/suport-birou-monitor-amxea-negru-pt-monitor-13-27-pana-la-7kg-brat-reglabil-ajustabil"
           "-m1/pd/D5DJJWBBM/")
driver.implicitly_wait(5)

# # how to keep the browser opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# the value attribute cand be added but the script can run without add just with the actual name of the class.
price_lei = driver.find_element(By.CLASS_NAME, value="product-new-price")
price_bani = driver.find_element(By.CLASS_NAME, "mf-decimal")

# sometimes the text you're trying to retrieve from an element might not be accessible through the .text property
# use .get_attribute("innerText") or .get_attribute("textContent")

# get all the text from the nested classes
test_price = price_lei.get_attribute("innerText")
print(test_price)

# find HTML elements by various tags
# name , class , id , Xpath, CSS Selector


driver.quit()
# # close will close just the active tab
# driver.close()
#
# # quit will close all the active tabs
# driver.quit()
