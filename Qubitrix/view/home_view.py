from Qubitrix.view.base_view import BaseView

class HomeView(BaseView):
    def render(self, screen):
        self.draw_text(screen, "Home Screen", (20, 20))
