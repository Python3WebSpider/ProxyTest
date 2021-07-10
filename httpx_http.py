import httpx

proxy = '127.0.0.1:7890'
proxies = {
    'http://': 'http://' + proxy,
    'https://': 'http://' + proxy,
}

with httpx.Client(proxies=proxies) as client:
    response = client.get('https://httpbin.org/get')
    print(response.text)
