from enum import Enum, auto
from Qubitrix.model.game_model import GameModel

class ViewType(Enum):
    HOME = auto()
    GAME = auto()
    PAUSE = auto()
    SUMMARY = auto()
    SETTINGS = auto()
    # Add more views as needed

class AppModel:
    """
    Tracks the current view/screen and holds references to sub-models (e.g., GameModel).
    """
    def __init__(self):
        self.current_view = ViewType.HOME
        self.game_model = None  # Will be set when a game starts
        # Add other sub-models as needed (e.g., settings_model)

    def start_game(self):
        self.game_model = GameModel(app_model=self)
        self.current_view = ViewType.GAME

    def go_home(self):
        self.current_view = ViewType.HOME
        self.game_model = None


    def pause_game(self):
        self.current_view = ViewType.PAUSE

    def resume_game(self):
        self.current_view = ViewType.GAME

    def show_summary(self):
        self.current_view = ViewType.SUMMARY

    def show_settings(self):
        self.current_view = ViewType.SETTINGS
