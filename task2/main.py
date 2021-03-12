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


counter = 0
url = driver.get('https://twitter.com/search?q=%23Winter')
formated_tags = []

def scrape_twitter(url, counter, formated_tags):
        try:
            element = WebDriverWait(driver, 10).until(
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
        next_url = driver.get(url)

        while counter < 6:
            counter += 1
            scrape_twitter(next_url, counter, formated_tags)

        driver.close()


scrape_twitter(url, counter, formated_tags)


"""


base_url = u'https://twitter.com/search?q='
query = u'%23Winter'
url = base_url + query
browser.get(url)

for _ in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

tweets = browser.find_elements_by_css_selector("[data-testid=\"tweet\"]")

bucket = {}

for tweet in tweets:
    bucket['text'] = tweet.text.format()
    bucket['url'] = tweet.
    #print(bucket)

    if len(bucket) < 6:
        # print(tweet.text)
        tags = driver.find_elements_by_xpath("//a[contains(@href,'hashtag')]")
        for tag in tags:
            print(f"----{tag.get_attribute('href')}")
            formated_tags.append(tag.get_attribute('href'))
            # print(formated_tags)

"""