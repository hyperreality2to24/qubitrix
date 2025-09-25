from Qubitrix.view.base_view import BaseView

class GameView(BaseView):
    def __init__(self, model=None):
        super().__init__()
        self.model = model

    def render(self, screen):
        self.draw_text(screen, "Game Screen", (20, 20))
        if self.model:
            self.draw_text(screen, f"[DEBUG] GameView.render called", (20, 60))
            self.draw_text(screen, f"Level: {getattr(self.model, 'level', 'N/A')}", (20, 100))
            self.draw_text(screen, f"Score: {getattr(self.model, 'score', 'N/A')}", (20, 140))
        else:
            self.draw_text(screen, "No game model attached", (20, 80))
