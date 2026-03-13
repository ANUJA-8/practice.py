#to run chromium + interpreter--- "playwright codegen website"
#to run a file "pytest -s test_rsauto.py --headed"
#for single test function run--- "pytest -s test_rsauto.py::test_automation --headed"
#to run all files start with name "test_" run "pytest"
from playwright.sync_api import Page, expect
import time
def test_automation(page:Page):
    #hide/display/click
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_role("textbox", name="Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_role("textbox", name="Hide/Show Example")).to_be_hidden()

#Alert boxes
    page.on("dialog", lambda dialog: dialog.accept())  #to accept the popup
    time.sleep(5)
    page.get_by_role("button", name="Confirm").click()
    # page.once("dialog", lambda dialog: dialog.dismiss()) #to dismiss the popup
    # page.get_by_role("button", name="Confirm").click()


#frame Handling
def test_frame_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("iframe[name=\"iframe-name\"]").content_frame.get_by_role("link", name="NEW All Access plan").click()
    expect(page.locator("iframe[name=\"iframe-name\"]").content_frame.get_by_role("heading", name="Join 13,522 Happy Subscibers!")).to_be_visible()
    time.sleep(5)

#web table handle
def test_web_table(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count()>0:
            colu=i
            print(colu)
            break
    rice_row=page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(colu)).to_have_text("37")

