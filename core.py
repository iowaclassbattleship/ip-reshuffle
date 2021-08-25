import configparser
from stem import Signal
from stem.control import Controller
import requests


class Network:
    def new_circuit(port, password):
        with Controller.from_port(port=port) as controller:
            controller.authenticate(password=password)
            controller.signal(Signal.NEWNYM)

    def get_session(httpProxy, httpsProxy):
        session = requests.session()
        session.proxies = {}
        session.proxies['http'] = httpProxy
        session.proxies['https'] = httpsProxy
        return session


class Config:
    def get_config(mode="DEFAULT"):
        config = configparser.ConfigParser()
        config.read("config.ini")
        return config["DEFAULT"]
