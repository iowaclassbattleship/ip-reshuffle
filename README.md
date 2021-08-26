# IP-reshuffle
[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Tor-logo-2011-flat.svg/1280px-Tor-logo-2011-flat.svg.png)](https://www.torproject.org/)

### Objective
Ip-reshuffle is supposed to grant you anonymity for any kind of requests you plan to make. Using tor the program will automatically change its IP-circuit to allow you to continue browsing safe from any harm.

### Use
You will have to have ```tor``` from the command line and set your password with ```tor --hash-password <password>``` and set the same password in the ```config.ini``` file. If you see the need to change the default ports and http(s) settings you can do this on your own behalf.

```python
session = core.Network.get_session(config["HttpProxy"], config["HttpsProxy"])

r = session.get("http://httpbin.org/ip")
```