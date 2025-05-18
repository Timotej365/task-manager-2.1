def test_odhlasenie(page):
    # Prihlásenie
    page.get_by_placeholder("Zadaj meno").fill("novytester123")
    page.get_by_placeholder("Zadaj heslo").fill("heslo123")
    page.get_by_role("button", name="Prihlásiť").click()
    page.wait_for_timeout(1500)

    # Klik na tlačidlo Odhlásiť
    page.get_by_role("button", name="Odhlásiť").click()
    page.wait_for_timeout(1500)

    # Over, že sa zobrazuje formulár (napr. text „Prihlásenie“)
    assert page.get_by_text("Prihlásenie").is_visible()
