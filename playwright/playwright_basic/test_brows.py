# def test_browse(playwright):
#     p=playwright.chromium.launch(headless=False)
#     c=p.new_context()
#     page=c.new_page()
#     page.goto("https://github.com/")

#to run a perticular function "pytest -s test_brows.py::test_child_window --headed"
from playwright.sync_api import Page, expect  # run as--" pytest -s test_brows.py --headed"
import time
def test_page(page:Page):   #it will run headless mode by default
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")#get_by_role used for many role based components 
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role(role="button", name="Sign In").click()
    # expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    page.get_by_role("link", name="iphone X").click()
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    page.get_by_role("link", name="Blackberry").click()
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    page.locator("app-card").filter(has_text="iphone X $24.99 Lorem ipsum").get_by_role("button").click()
    page.locator("app-card").filter(has_text="Nokia Edge $24.99 Lorem ipsum").get_by_role("button").click()
    page.get_by_text("Checkout ( 2 ) (current)").click()
    expect(page.locator(".media-body")).to_have_count(2)
    
def test_child_window(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Free Access to InterviewQues/").click()
        page1 = page1_info.value
        text=page1.get_by_role("link", name="mentor@rahulshettyacademy.com").text_content()
        print(text)
        assert text== "mentor@rahulshettyacademy.com"
    time.sleep(5)

