from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(proxy={
        'server': 'http://127.0.0.1:7890',
        'username': 'foo',
        'password': 'bar'
    })
    page = browser.new_page()
    page.goto('https://httpbin.org/get')
    print(page.content())
    browser.close()
