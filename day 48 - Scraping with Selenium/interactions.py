import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# set the url
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Chrome()
# set a window size
driver.set_window_size(1500, 900)
driver.get(URL)
driver.implicitly_wait(10)
# extract the text of the element
articles_number_element = driver.find_element(By.ID, "articlecount").text
# split by spaces
number = articles_number_element.split(" ")
# print index 0 to get the challenge result
print(number[0])

# find the search bar and type some stuff inside
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(2)
# find a link and click on it
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
all_portals.click()

driver.quit()
