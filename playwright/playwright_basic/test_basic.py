def test_playwright(playwright): #playwright is an fixture here and no need to create function for this as this is an in build function
    browser= playwright.chromium.launch(headless=False)  #invoke headed chrome engine 
    context= browser.new_context()
    page= context.new_page()
    page.goto("https://www.udemy.com/")