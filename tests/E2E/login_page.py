class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://task-manager-2-1.vercel.app/"

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.page.get_by_placeholder("Zadaj meno").fill(username)
        self.page.get_by_placeholder("Zadaj heslo").fill(password)
        self.page.get_by_role("button", name="Prihlásiť").click()
        # Počkajte krátky čas, aby sa UI aktualizovalo
        self.page.wait_for_timeout(1000)

    def is_logged_in(self) -> bool:
        return self.page.locator("h2:has-text('Nezahájené úlohy')").is_visible()

    def get_error_message(self) -> str:
        # Vyberieme text z <div> chybovej hlášky (napr. s class="error")
        return self.page.locator("div.error").inner_text()
