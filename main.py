import core

config = core.Config.get_config()
core.Network.new_circuit(int(config["Port"]), config["ControllerPassword"])

session = core.Network.get_session(config["HttpProxy"], config["HttpsProxy"])

r = session.get("http://httpbin.org/ip")

print(r.text)
