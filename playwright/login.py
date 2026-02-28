from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set True in CI
        page = browser.new_page()

        # Open website      
        page.goto("https://the-internet.herokuapp.com/login")

        # Enter credentials
        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")

        # Click login button
        page.click("button[type='submit']")

        # Verify successful login
        success_message = page.locator("#flash").text_content()
        print(success_message)

        assert "You logged into a secure area!" in success_message

        browser.close()

run()