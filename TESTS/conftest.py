import pytest
from playwright.sync_api import sync_playwright
from server_ready import cakat_na_server

BASE_URL = "https://task-manager-2-1.vercel.app"  # frontend URL

@pytest.fixture(scope="session", autouse=True)
def priprav_server():
    print("⏳ Prebieha prebudenie servera Render...")
    cakat_na_server()
    print("✅ Server je pripravený. Pokračujeme v testoch.")

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)  # Naviguj na moju stránku
        yield page
        browser.close()
