import requests

proxy = '127.0.0.1:7890'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy,
}
try:
    response = requests.get('https://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)