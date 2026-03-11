import time
from playwright.sync_api import Page, expect  # run as--" pytest -s test_brows.py --headed"

def test_browse(playwright):
    p=playwright.firefox.launch(headless=False)
    page=p.new_page()  
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("aLearning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")#get_by_role used for many role based components 
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role(role="button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    # error_message = page.locator("Incorrect username/password.")
    # expect(error_message).to_be_visible()
    # expect(page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")
    time.sleep(5)
