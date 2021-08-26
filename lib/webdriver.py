from selenium import webdriver


def setup_driver(profile=None):
    return webdriver.Firefox(profile)


def profile(httpProxy):
    profile = webdriver.FirefoxProfile()
    _, proxy = httpProxy.split("//")
    ip, port = proxy.split(':')
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', ip)
    profile.set_preference('network.proxy.socks_port', int(port))
    return profile


def test_tor(driver):
    driver.get("https://check.torproject.org/")


def test_useragent(driver):
    driver.get("https://whatmyuseragent.com/")


def get(driver, url):
    driver.get(url)


def close(driver):
    driver.close()
