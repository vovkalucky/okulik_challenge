from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class MainPage(BasePage):
    url = "https://demoblaze.com/"