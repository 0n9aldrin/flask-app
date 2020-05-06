from flask import Flask
from selenium import webdriver
import os

app = Flask(__name__)


@app.route('/')
def index():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get('https://stackoverflow.com/questions/19035186/how-to-select-element-using-xpath-syntax-on-selenium-for-python')
    title = driver.find_element_by_xpath('//*[@id="question"]/div[2]/div[2]/div[1]/p[1]')
    return title.text


if __name__ == "__main__":
    app.run()