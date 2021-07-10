from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = 'username:password@127.0.0.1:7890'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
