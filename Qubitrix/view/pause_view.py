from Qubitrix.view.base_view import BaseView

class PauseView(BaseView):
    def __init__(self, app_model=None):
        super().__init__()
        self.app_model = app_model

    def render(self, screen):
        self.draw_text(screen, "Pause Screen", (20, 20))
        self.draw_text(screen, "Press R to resume", (20, 80))
        self.draw_text(screen, "Q: Quit", (20, 120))