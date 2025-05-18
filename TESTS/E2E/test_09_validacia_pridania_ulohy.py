def test_validacia_pridania_ulohy(page):
    # Prihlásenie
    page.get_by_placeholder("Zadaj meno").fill("novytester123")
    page.get_by_placeholder("Zadaj heslo").fill("heslo123")
    page.get_by_role("button", name="Prihlásiť").click()
    page.wait_for_timeout(2000)

    # Zadaj len názov bez popisu
    page.get_by_placeholder("Zadaj názov").fill("Test bez popisu")
    page.get_by_role("button", name="Pridať").click()
    page.wait_for_timeout(1000)
    assert "Zadaj názov aj popis." in page.content()

    # Vymaž názov a zadaj len popis bez názvu
    page.get_by_placeholder("Zadaj názov").fill("")
    page.get_by_placeholder("Zadaj popis").fill("Len popis")
    page.get_by_role("button", name="Pridať").click()
    page.wait_for_timeout(1000)
    assert "Zadaj názov aj popis." in page.content()

    # Nezadané nič
    page.get_by_placeholder("Zadaj popis").fill("")
    page.get_by_role("button", name="Pridať").click()
    page.wait_for_timeout(1000)
    assert "Zadaj názov aj popis." in page.content()
