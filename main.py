import sys

from lib import core
from lib import webdriver

config = core.Config.get_config()
driver = webdriver.setup_driver(webdriver.profile(config["HttpProxy"]))


def parse_input(line):
    if line == "q":
        return False
    elif line == "close":
        webdriver.close(driver)
    return True


for line in sys.stdin:
    if not parse_input(line.rstrip()):
        break
