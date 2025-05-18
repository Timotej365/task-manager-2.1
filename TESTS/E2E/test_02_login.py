def test_login(page):
    # Počkaj na zobrazenie prihlasovacieho poľa max 15 sekúnd
    page.wait_for_selector("input[placeholder='Zadaj meno']", timeout=15000)

    # Vyplň údaje
    page.get_by_placeholder("Zadaj meno").fill("novytester123")
    page.get_by_placeholder("Zadaj heslo").fill("heslo123")
    page.get_by_role("button", name="Prihlásiť").click()

    # Po prihlásení skontroluj meno používateľa
    page.wait_for_selector("text=👤 novytester123", timeout=5000)
    assert page.get_by_text("👤 novytester123").is_visible()
