from lib import core
from lib import webdriver

config = core.Config.get_config()
core.Network.new_circuit(int(config["Port"]), config["ControllerPassword"])

driver = webdriver.setup_driver(webdriver.profile(config["HttpProxy"]))

webdriver.test_tor(driver)
