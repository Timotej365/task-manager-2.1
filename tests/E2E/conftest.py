import pytest
from playwright.sync_api import sync_playwright, Page, Browser

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def page(playwright_instance) -> Page:
    browser = playwright_instance.chromium.launch(headless=True, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()
    try:
        yield page
    finally:
        context.close()
        browser.close()

