from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

# not a fan of time.sleep() so i dont use it unless I need to see something in the code

google_form_url = "https://forms.gle/hwoxRyexibYTrbhG6"
scrape_source_url = "https://appbrewery.github.io/Zillow-Clone/"


# scrape the data from the requested links
scrape_response = requests.get(scrape_source_url)
data_scrape = scrape_response.text
soup_scrape = BeautifulSoup(data_scrape, "html.parser")

# identify the images we need the links to of - get the anchor tags of the images
images_soup = soup_scrape.select(".StyledPropertyCardPhotoBody a")

# list comprehension them to arrange them
all_links = [link["href"] for link in images_soup]
# print(all_links)  # print statement to check the code


# #### get the address list
addresses_soup = soup_scrape.select(".StyledPropertyCardDataWrapper address")
# list comprehension get text -> replace the | with spaces and then strip
address_list = [address.get_text().replace(" | ", " ").strip() for address in addresses_soup]
# print(address_list)  # print statement to check the code

# #### get the price of the property
price_soup = soup_scrape.find_all("div", class_="PropertyCardWrapper")

# --> for loop solution <-- #
all_prices = []

for price in price_soup:
    # check for a "$"
    if "$" in price.text:
        # extract the text , remove the /mo part
        clean_price = price.get_text().replace("/mo", "").split("+")[0]
        # append the items
        all_prices.append(clean_price)

# --> list comprehension solution <-- #
# all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in price_soup if "$" in price.text]

# print(all_prices) # print statement to check the code

# #### Selenium part ####
driver = webdriver.Chrome()
driver.get(google_form_url)
driver.set_window_size(1500, 1000)
driver.implicitly_wait(15)

# find input fields based on XPATH , forms input fields do not have separate id /class / etc

for n in range(len(all_links)):
    q1_input = driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
    )
    q2_input = driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
    )
    q3_input = driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"
    )
    submit_button = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")

    q1_input.send_keys(address_list[n])
    q2_input.send_keys(all_prices[n])
    q3_input.send_keys(all_links[n])
    submit_button.click()
    new_answer_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    new_answer_button.click()

driver.quit()
