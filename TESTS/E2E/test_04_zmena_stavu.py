def test_zmena_stavu_ulohy(page):
    # Prihlásenie
    page.get_by_placeholder("Zadaj meno").fill("novytester123")
    page.get_by_placeholder("Zadaj heslo").fill("heslo123")
    page.get_by_role("button", name="Prihlásiť").click()
    page.wait_for_timeout(2000)

    # Zmena stavu úlohy
    page.get_by_role("button", name="Prebieha").nth(0).click()
    page.wait_for_timeout(2000)

    # Overenie
    assert "Prebiehajúce úlohy" in page.content()
