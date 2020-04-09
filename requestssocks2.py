import requests
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 7891)
socket.socket = socks.socksocket
try:
    response = requests.get('https://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)