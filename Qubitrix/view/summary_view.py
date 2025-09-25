from Qubitrix.view.base_view import BaseView

class SummaryView(BaseView):
    def render(self, screen):
        self.draw_text(screen, "Summary Screen", (20, 20))
