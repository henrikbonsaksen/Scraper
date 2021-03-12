import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import random

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)

start_url = driver.get('https://twitter.com/search?q=%23Winter%27')
counter = 0
formatted_tags = []


def get_tags(url):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'hashtag')]")))

    except TimeoutException:
        print("Could not find element")

    finally:
        tags = driver.find_elements_by_xpath("//a[contains(@href,'hashtag')]")

        for tag in tags:
            print(f"----{tag.get_attribute('href')}")
            formatted_tags.append(tag.get_attribute('href'))

    return formatted_tags


get_tags(start_url)

while counter < 6:
    counter += 1
    print(6 - counter, "pages left to visit")
    next_url = random.choice(formatted_tags)
    print("Next page: ", next_url)
    formatted_tags = []
    next_page = driver.get(next_url)
    get_tags(next_page)
driver.close()
