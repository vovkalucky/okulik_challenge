from pages.base_page import BasePage


class MagentoPage(BasePage):
    url = "https://magento.softwaretestingboard.com/gear/bags.html"

    def collect_price(self):
        elements = self.page.locator("[id^='product-price-'] span")
        count = elements.count()
        prices = []
        for i in range(count):
            el = elements.nth(i)
            prices.append(el.text_content()[1:])
        print(f"\n{prices}\n")
