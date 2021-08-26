from selenium import webdriver


def setup_driver():
    return webdriver.Firefox()


def test(driver, url):
    driver.get(url)


def close(driver):
    driver.close()
