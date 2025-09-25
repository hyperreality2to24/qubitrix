from Qubitrix.model.app_model import ViewType
from Qubitrix.view.home_view import HomeView
from Qubitrix.view.game_view import GameView
from Qubitrix.view.pause_view import PauseView
from Qubitrix.view.summary_view import SummaryView
from Qubitrix.view.settings_view import SettingsView

class AppView:
    """
    Central view manager for Qubitrix.
    Responsible for instantiating and returning the correct view object for each application state (HOME, GAME, PAUSE, SUMMARY, SETTINGS).
    Each view handles its own rendering logic, typically via a `render(screen)` method for Pygame output.
    AppView acts as a factory and router, ensuring the right view is used for the current state.
    """
    def __init__(self, app_model):
        self.app_model = app_model

    def get_view(self, view_type):
        if view_type == ViewType.HOME:
            return HomeView(app_model=self.app_model)
        elif view_type == ViewType.GAME:
            # Always inject the current GameModel
            return GameView(self.app_model.game_model)
        elif view_type == ViewType.PAUSE:
            return PauseView(app_model=self.app_model)
        elif view_type == ViewType.SUMMARY:
            return SummaryView()
        elif view_type == ViewType.SETTINGS:
            return SettingsView()
        else:
            print(f"[ERROR] No view found for {view_type}. Showing HomeView.")
            return HomeView(app_model=self.app_model)
