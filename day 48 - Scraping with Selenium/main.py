from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1000, 800)

URL = "https://www.python.org/"

driver.get(URL)
driver.implicitly_wait(10)

upcoming_events = driver.find_element(By.XPATH, "//*[@id='content']/div/section/div[2]/div[2]/div/ul")
text_data = upcoming_events.get_attribute("innerText")
# print(text_data)
test1 = text_data.split("\n")
# print(test1)
# extracting keys at even indices
dict_keys = test1[::2]
# extract values at odd indices
dict_values = test1[1::2]
# print statements to check the results
"""" you cant have the same key in a dictionary !!! even if it has different values """
# print(dict_keys)  # # if there are some keys that are repeating you cant transfer the data in a dictionary
# print(dict_values)

result_list = []
for i in range(0, len(test1), 2):
    result_list.append(test1[i:i + 2])

print(result_list)

driver.quit()
