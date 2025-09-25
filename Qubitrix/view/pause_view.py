from Qubitrix.view.base_view import BaseView

class PauseView(BaseView):
    def render(self, screen):
        self.draw_text(screen, "Pause Screen", (20, 20))
