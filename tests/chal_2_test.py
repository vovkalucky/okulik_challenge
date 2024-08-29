from playwright.sync_api import Page
from pages.chal_2_page import MagentoPage
import allure


@allure.title("Получить цену товаров")
def test_get_price(page: Page):
    page = MagentoPage(page)
    page.open_page()
    page.collect_price()