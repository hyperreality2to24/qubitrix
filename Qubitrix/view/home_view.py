from Qubitrix.view.base_view import BaseView

class HomeView(BaseView):
    def __init__(self, app_model=None):
        super().__init__()
        self.app_model = app_model

    def render(self, screen):
        self.draw_text(screen, "Home Screen", (20, 20))
        self.draw_text(screen, "G: Start Game", (20, 80))
        self.draw_text(screen, "T: Settings", (20, 120))
        self.draw_text(screen, "Q: Quit", (20, 200))
