from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    m=p.chromium.launch(headless=False)
    page=m.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")

    page.wait_for_url("https://demo.automationtesting.in/Alerts.html")
    page.once('dialog',lambda dialog:dialog.accept())
    page.locator('//button[@onclick="alertbox()"]').click()
    page.wait_for_timeout(2000)
    #page.wait_for_timeout(5000)

    #page.on("dialog",lambda x:x.accept())
    
    page.locator('//a[@href="#CancelTab"]').click()
    page.once("dialog",lambda dialog:dialog.dismiss())

    page.locator('//button[@onclick="confirmbox()"]').click()
    page.wait_for_timeout(2000)
    

    page.locator('//a[@href="#Textbox"]').click()
    page.once("dialog",lambda dialog:dialog.accept("Manash"))
    page.locator('//button[@onclick="promptbox()"]').click()
    
    page.wait_for_timeout(5000)
