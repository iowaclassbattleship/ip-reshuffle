import sys
from enum import Enum

from lib import core
from lib import webdriver

class Command(Enum):
    QUIT = "000"
    OPEN = "100"
    CLOSE = "200"
    SEARCH = "300"
    CIRCUIT = "400"

config = core.Config.get_config()
driver = webdriver.setup_driver(webdriver.profile(config["HttpProxy"]))

def parse_input(line):
    if line == "q" or line == Command.QUIT.value:
        webdriver.close(driver)
        return False
    elif line == Command.CLOSE.value:
        webdriver.close(driver)
        sys.stdout.write("Selenium browser closed\n")
    elif line == Command.SEARCH.value:
        webdriver.get(driver, "https://www.hashemian.com/whoami/")
        sys.stdout.write("Search conducted\n")
    elif line == Command.CIRCUIT.value:
        core.Network.new_circuit(config["ControllerPassword"])
        sys.stdout.write("New circuit\n")
    return True


for line in sys.stdin:
    if not parse_input(line.rstrip()):
        break