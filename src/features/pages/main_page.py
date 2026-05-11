
class MainPage:
    def __init__(self, base_url, page):
        self.base_url = base_url
        self.page = page
        self.add_player_button = page.get_by_role("button", name="Lägg till spelare")

    # more methods as we go

    def navigate(self):
        self.page.goto(self.base_url, timeout=5000)

    def click_add_player_button(self):
        self.add_player_button.click()