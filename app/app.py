from selenium import webdriver
import logging
import os

logging.getLogger().setLevel(logging.INFO)


def lambda_handler(event, context):
    logging.info("python-selenium-chromium-on-lambda started")

    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "/tmp", "safebrowsing.enabled": True}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-translate")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1600,1024")
    chrome_options.add_argument("--disable-impl-side-painting")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(60)

    open_google(driver)
    take_screenshot(driver, "screenshot_google.png")
    driver.close()

    return


def open_google(driver):
    logging.info("opening google...")
    url = "https://google.com"
    driver.get(url)


def take_screenshot(driver, filename):
    logging.info(f"taking screenshot {filename}...")
    driver.save_screenshot(filename)
    logging.info(f"screenshot location: {os.getcwd()}/{filename}")
