import allure

from pages.base_page import BasePage

PRICE = "[id^='product-price-'] > span"


class MagentoPage(BasePage):
    url = "https://magento.softwaretestingboard.com/gear/bags.html"

    def collect_price(self):
        with allure.step("Сбор цен товаров"):
            elements = self.page.locator(PRICE)
            prices = []
            for el in elements.all():
                prices.append(el.text_content()[1:])
            print(f"\n{prices}\n")