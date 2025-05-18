import pytest

@pytest.mark.parametrize("nazov, popis", [
    ("Test úloha A", "Popis A"),
    ("Úloha s dĺžňami", "Popis s diakritikou: žluťoučký kůň"),
    ("Zložitejší názov úlohy", "123456"),
])
def test_pridanie_a_odstranenie_ulohy(page, nazov, popis):
    # Prihlásenie
    page.get_by_placeholder("Zadaj meno").fill("novytester123")
    page.get_by_placeholder("Zadaj heslo").fill("heslo123")
    page.get_by_role("button", name="Prihlásiť").click()
    page.wait_for_timeout(2000)

    # Pridanie úlohy
    page.get_by_placeholder("Zadaj názov").fill(nazov)
    page.get_by_placeholder("Zadaj popis").fill(popis)
    page.get_by_role("button", name="Pridať").click()
    page.wait_for_timeout(2000)

    # Overenie, že sa úloha objavila
    assert nazov in page.content()
    assert popis in page.content()

    # Vymazanie úlohy
    page.get_by_role("button", name="Odstrániť").nth(0).click()
    page.get_by_role("button", name="Áno").click()

    # Počkaj, kým zmizne z DOMu
    page.wait_for_selector(f"text={nazov}", state="detached", timeout=5000)

    # Overenie, že sa úloha už nenachádza
    assert nazov not in page.content()
