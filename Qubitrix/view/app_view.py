from Qubitrix.model.app_model import ViewType
from Qubitrix.view.home_view import HomeView
from Qubitrix.view.game_view import GameView
from Qubitrix.view.pause_view import PauseView
from Qubitrix.view.summary_view import SummaryView
from Qubitrix.view.settings_view import SettingsView

class AppView:
    def __init__(self, app_model):
        self.app_model = app_model

    def get_view(self, view_type):
        if view_type == ViewType.HOME:
            return HomeView()
        elif view_type == ViewType.GAME:
            # Always inject the current GameModel
            return GameView(self.app_model.game_model)
        elif view_type == ViewType.PAUSE:
            return PauseView()
        elif view_type == ViewType.SUMMARY:
            return SummaryView()
        elif view_type == ViewType.SETTINGS:
            return SettingsView()
        else:
            print(f"[ERROR] No view found for {view_type}. Showing HomeView.")
            return HomeView()
