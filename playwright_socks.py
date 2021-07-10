from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(proxy={
        'server': 'socks5://127.0.0.1:7891'
    })
    page = browser.new_page()
    page.goto('https://httpbin.org/get')
    print(page.content())
    browser.close()
