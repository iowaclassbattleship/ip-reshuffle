from lib import core
from lib import webdriver

config = core.Config.get_config()
core.Network.new_circuit(int(config["Port"]), config["ControllerPassword"])

session = core.Network.get_session(config["HttpProxy"], config["HttpsProxy"])

r = session.get("http://httpbin.org/ip")

print(r.text)
driver = webdriver.setup_driver()

webdriver.test(driver, "https://www.wikipedia.org")
webdriver.test(driver, "https://www.google.com")
webdriver.test(driver, "https://www.wikipedia.org")
webdriver.test(driver, "https://www.google.com")
webdriver.test(driver, "https://www.wikipedia.org")
