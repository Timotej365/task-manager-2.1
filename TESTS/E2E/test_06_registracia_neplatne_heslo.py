def test_registracia_neplatne_heslo(page):
    # Prepnutie na registráciu
    page.get_by_role("button", name="Registrovať sa").click()

    # Vyplnenie formulára s neplatným heslom (príliš krátke)
    page.get_by_placeholder("Zadaj meno").fill("neplatneheslo")
    page.get_by_placeholder("Zadaj heslo").fill("123")

    # Pokus o registráciu
    page.get_by_role("button", name="Registrovať").click()

    # Overenie, že sa zobrazila chyba o hesle
    page.wait_for_timeout(1000)
    obsah = page.locator(".error").text_content()
    assert "Heslo musí mať aspoň 6 znakov" in obsah
