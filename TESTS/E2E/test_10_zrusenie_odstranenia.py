def test_zrusenie_odstranenia(page):
    # Prihlásenie
    page.get_by_placeholder("Zadaj meno").fill("novytester123")
    page.get_by_placeholder("Zadaj heslo").fill("heslo123")
    page.get_by_role("button", name="Prihlásiť").click()
    page.wait_for_timeout(1500)

    # Pridaj novú úlohu
    page.get_by_placeholder("Zadaj názov").fill("Test úloha na zrušenie")
    page.get_by_placeholder("Zadaj popis").fill("Popis úlohy")
    page.get_by_role("button", name="Pridať").click()
    page.wait_for_timeout(1000)

    # Klikni na "Odstrániť"
    page.get_by_role("button", name="Odstrániť").nth(0).click()
    # Klikni na "Zrušiť"
    page.get_by_role("button", name="Zrušiť").click()
    page.wait_for_timeout(1000)

    # Skontroluj, že úloha tam stále je
    assert page.get_by_text("Test úloha na zrušenie").is_visible()

    # Reálne odstráň úlohu
    page.get_by_role("button", name="Odstrániť").nth(0).click()
    page.get_by_role("button", name="Áno").click()
    page.wait_for_timeout(1000)

    # Over, že úloha bola odstránená
    assert "Test úloha na zrušenie" not in page.content()
