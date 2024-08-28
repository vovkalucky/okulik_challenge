from playwright.sync_api import Page


class BasePage:
    url = None
    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.url:
            self.page.goto(self.url, wait_until='domcontentloaded')
        else:
            print('Not possible to open page without url')

    def click_button_by_role(self, name):
        self.page.get_by_role("link", name=name).click()

