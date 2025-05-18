def test_zobrazenie_mena_pouzivatela(page):
    # Prihlásenie
    page.get_by_placeholder("Zadaj meno").fill("novytester123")
    page.get_by_placeholder("Zadaj heslo").fill("heslo123")
    page.get_by_role("button", name="Prihlásiť").click()
    page.wait_for_timeout(1500)

    # Skontroluj, že sa zobrazuje meno používateľa
    obsah = page.content()
    assert "novytester123" in obsah
