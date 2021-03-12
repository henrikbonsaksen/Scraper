from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
import random

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='chromedriver', options=chrome_options)
driver.wait = WebDriverWait(driver, 10)


counter = 0
url = driver.get("https://twitter.com/search?q=%23Winter")
formated_tags = []


def scrape_twitter(url, counter, formated_tags):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'hashtag')]"))
        )

    finally:
        tags = driver.find_elements_by_xpath("//a[contains(@href,'hashtag')]")
        for tag in tags:
            print(f"----{tag.get_attribute('href')}")
            formated_tags.append(tag.get_attribute('href'))

        print(6 - counter, "pages to visit")

        url = random.choice(formated_tags)
        url = str(url)
        print("next url to visit: ", str(url))

    while counter < 6:
        counter += 1
        scrape_twitter(url, counter, formated_tags)


scrape_twitter(url, counter, formated_tags)

driver.close()
