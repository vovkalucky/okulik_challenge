import pytest
from playwright.sync_api import sync_playwright


# Параметризуем фикстуру для использования всех браузеров
@pytest.fixture(params=["chromium", "firefox", "webkit"]) #, "firefox", "webkit"
def browser(request):
    with sync_playwright() as p:
        browser = p[request.param].launch()
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page
    context.close()