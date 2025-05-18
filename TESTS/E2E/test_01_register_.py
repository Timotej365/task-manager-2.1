def test_register_user(page):
    # Klikni na odkaz „Registrovať sa“
    page.get_by_text("Registrovať sa").click()

    # Počkaj na nápis „Registrácia“ (titulok)
    page.get_by_role("heading", name="Registrácia").wait_for(timeout=5000)

    # Vyplň prihlasovacie údaje
    page.get_by_label("Používateľské meno").fill("novytester123")
    page.get_by_label("Heslo").fill("heslo123")

    # Klikni na modré tlačidlo „Registrovať“
    page.get_by_role("button", name="Registrovať").click()

    # Očakávaj zmenu formulára alebo správu
    page.wait_for_timeout(1500)
    assert "Registrácia bola úspešná" in page.content()
