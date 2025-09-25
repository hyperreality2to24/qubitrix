from Qubitrix.view.base_view import BaseView

class SettingsView(BaseView):
    def render(self, screen):
        self.draw_text(screen, "Settings Screen", (20, 20))
