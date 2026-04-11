import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("Learning@830$3mK2")
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
