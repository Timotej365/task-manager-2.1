def test_prihlasenie_bez_udajov(page):
    # Prihlásenie bez vyplnenia údajov
    page.get_by_role("button", name="Prihlásiť").click()

    # Overenie chybovej hlášky
    page.wait_for_timeout(1000)
    obsah = page.locator(".error").text_content()
    assert "Zadaj meno aj heslo." in obsah
