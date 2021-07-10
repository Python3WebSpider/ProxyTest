import httpx
from httpx_socks import SyncProxyTransport

transport = SyncProxyTransport.from_url(
    'socks5://127.0.0.1:7891')

with httpx.Client(transport=transport) as client:
    response = client.get('https://httpbin.org/get')
    print(response.text)
