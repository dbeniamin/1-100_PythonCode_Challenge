import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome()
driver.set_window_size(1500, 900)
driver.get(URL)
driver.implicitly_wait(10)

# get the cookie element
cookie_element = driver.find_element(By.XPATH, "//*[@id='cookie']")

# store stuff
cursor_element = driver.find_element(By.ID, "buyCursor")
grandma_element = driver.find_element(By.ID, "buyGrandma")
factory_element = driver.find_element(By.ID, "buyFactory")
mine_element = driver.find_element(By.ID, "buyMine")
shipment_element = driver.find_element(By.ID, "buyShipment")
alchemy_lab_element = driver.find_element(By.ID, "buyAlchemy lab")
portal_element = driver.find_element(By.ID, "buyPortal")
time_machine_element = driver.find_element(By.ID, "buyTime machine")

ELEMENT_LIST = [
    cursor_element,
    grandma_element,
    factory_element,
    mine_element,
    shipment_element,
    alchemy_lab_element,
    portal_element,
    time_machine_element
]


def click_element_continuously(element, duration):
    count_time_end = time.time() + duration
    while time.time() < count_time_end:
        element.click()


# function to get the current cookie count
def get_cookie_count():
    money_count_element = driver.find_element(By.ID, "money").text
    if "," in money_count_element:
        money_count_element = money_count_element.replace(",", "")
    return int(money_count_element)


# main loop of the script
end_time = time.time() + 300  # set the time to run for the script

while time.time() < end_time:
    # get all prices
    all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
    item_prices = []

    # extract all prices
    for price in all_prices:
        element_text = price.text
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    # get current cookie count
    cookie_count = get_cookie_count()

    # find max affordable upgrade and the index of it
    max_affordable_index = -1
    for index, price in enumerate(item_prices):
        if cookie_count >= price:
            max_affordable_index = index

    # click the specific element
    if max_affordable_index != -1 and max_affordable_index != 0:
        element_to_click = all_prices[max_affordable_index].find_element(By.XPATH, "..")
        element_to_click.click()

    # continuous click the cookie for a set period of time - in seconds - before checking again the upgrades
    click_element_continuously(cookie_element, 5)

# get the final element and print the score
cps_element = driver.find_element(By.ID, "cps").text
print(cps_element)

driver.quit()
