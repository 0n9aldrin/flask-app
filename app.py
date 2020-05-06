from flask import Flask
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


app = Flask(__name__)


@app.route('/')
def index():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://shopee.co.id/search?keyword=calculator")
    actions = ActionChains(driver)

    for x in range(7):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)

    name = driver.find_elements_by_css_selector("#main > div > div.shopee-page-wrapper > div.container._2_Y1cV > div.jrLh5s > div.shopee-search-item-result > div.row.shopee-search-item-result__items > div > div > a > div > div:nth-child(2) > div:nth-child(1) > div")

    names = ''
    for x in range(len(name)):
        names = names + name[x].text
    names = names + str(len(name))
    
    return names


if __name__ == "__main__":
    app.run()