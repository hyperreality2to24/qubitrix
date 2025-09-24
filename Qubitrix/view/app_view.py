from Qubitrix.model.app_model import ViewType
from Qubitrix.view.home_view import HomeView
from Qubitrix.view.game_view import GameView
from Qubitrix.view.pause_view import PauseView
from Qubitrix.view.summary_view import SummaryView
from Qubitrix.view.settings_view import SettingsView

class AppView:
    def __init__(self):
        self._view_map = {
            ViewType.HOME: HomeView(),
            ViewType.GAME: GameView(),
            ViewType.PAUSE: PauseView(),
            ViewType.SUMMARY: SummaryView(),
            ViewType.SETTINGS: SettingsView(),
        }

    def get_view(self, view_type):
        view = self._view_map.get(view_type)
        if view is None:
            print(f"[ERROR] No view found for {view_type}. Showing HomeView.")
            return self._view_map[ViewType.HOME]
        return view
