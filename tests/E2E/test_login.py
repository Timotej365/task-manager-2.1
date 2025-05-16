import pytest
from .login_page import LoginPage

# POZITÍVNY TEST
@pytest.mark.parametrize("username, password", [
    ("testing", "testing1")
])
def test_login_success(page, username, password):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)
    assert login.is_logged_in()

# NEGATÍVNE TESTY
@pytest.mark.parametrize("username, password, expected_error", [
    ("", "", "Zadaj meno aj heslo."),
    ("student", "zleheslo", "Prihlásenie zlyhalo.")
])
def test_login_failures(page, username, password, expected_error):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)

    # Počkáme na zobrazenie chyby v DOM
    error_message = login.get_error_message()
    assert expected_error in error_message
