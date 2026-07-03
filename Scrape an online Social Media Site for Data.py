from playwright.sync_api import sync_playwright

command prompt: pip install playwright
                py -m pip install playwright 

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://x.com/OpenAI")

    page.wait_for_timeout(5000)

    print(page.title())

    browser.close()
