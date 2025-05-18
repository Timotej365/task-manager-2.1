def test_odstranenie_ulohy(page):
    # Prihlásenie
    page.get_by_placeholder("Zadaj meno").fill("novytester123")
    page.get_by_placeholder("Zadaj heslo").fill("heslo123")
    page.get_by_role("button", name="Prihlásiť").click()
    page.wait_for_timeout(1000)

    # Počkaj, kým sa objaví aspoň jedna úloha s tlačidlom „Odstrániť“
    page.get_by_role("button", name="Odstrániť").nth(0).wait_for(timeout=5000)

    # Klikni na „Odstrániť“ a potvrď modal
    page.get_by_role("button", name="Odstrániť").nth(0).click()
    page.get_by_role("button", name="Áno").click()

    # Počkaj na aktualizáciu
    page.wait_for_timeout(1500)

    # Over, že už na stránke nie je žiadne tlačidlo „Odstrániť“ (aspoň prvé zmizlo)
    assert page.locator("text=Odstrániť").count() == 0 or not page.get_by_role("button", name="Odstrániť").is_visible()
