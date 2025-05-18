def test_pridanie_ulohy(page):
    # Prihlásenie
    page.get_by_placeholder("Zadaj meno").fill("novytester123")
    page.get_by_placeholder("Zadaj heslo").fill("heslo123")
    page.get_by_role("button", name="Prihlásiť").click()
    page.wait_for_timeout(2000)

    # Pridanie úlohy
    page.get_by_placeholder("Zadaj názov").fill("Testovacia úloha")
    page.get_by_placeholder("Zadaj popis").fill("Popis úlohy")
    page.get_by_role("button", name="Pridať").click()
    page.wait_for_timeout(2000)

    # Overenie
    assert "Testovacia úloha" in page.content()
