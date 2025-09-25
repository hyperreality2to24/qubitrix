from Qubitrix.view.base_view import BaseView

class GameView(BaseView):
    def __init__(self, model=None):
        super().__init__()
        self.model = model

    def render(self, screen):
        self.draw_text(screen, "Game Screen", (20, 20))
