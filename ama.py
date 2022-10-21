import articles as articles
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https:amazon.in")

search = driver.find_element_by_name('field-keywords')
driver.find_element_by_id("nav-search-submit-button").click()
search.send_keys("laptop")
search.send_keys(Keys.RETURN)
driver.find_element_by_class_name("s-image")


# try:
#     productTitle = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "productTitle"))
#     )
#     articles = main.find_elements_by_id("ppd")
#     for article in articles:
#         header = article.find_element_by_class_name("a-list-item")
#         print(header.text)
# finally:
# # driver.quit()
#
print(productTitle)

