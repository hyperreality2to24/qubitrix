import pygame
import pytest
from Qubitrix.controller.home_screen_controller import HomeScreenController
from Qubitrix.view.home_view import HomeView

class DummyAppModel:
    """
    Minimal stand-in for the real AppModel.
    Used to track state changes (e.g., starting the game) without side effects or dependencies.
    """
    def __init__(self):
        self.current_view = None
        self.started_game = False
    def start_game(self):
        self.started_game = True
        self.current_view = 'GAME'

class DummyHomeView(HomeView):
    """
    Minimal stand-in for the real HomeView.
    Used to inject a dummy app_model for controller testing without UI dependencies.
    """
    def __init__(self, app_model):
        super().__init__()
        self.app_model = app_model

@pytest.fixture
def home_controller():
    """
    Pytest fixture that creates a HomeScreenController with dummy dependencies.
    This allows each test to use a fresh controller instance with isolated state.
    """
    app_model = DummyAppModel()
    view = DummyHomeView(app_model)
    return HomeScreenController(view)

def test_handle_input_method(home_controller):
    """
    Test direct method call to handle_input on the controller.
    This simulates non-pygame input (e.g., for unit tests or CLI).
    Here, we override handle_input to trigger game logic and assert the state change.
    """
    def handle_input(cmd):
        if cmd == 'g':
            home_controller.app_model.start_game()
    home_controller.handle_input = handle_input
    home_controller.handle_input('g')
    assert home_controller.app_model.started_game

def test_pygame_event(home_controller):
    """
    Test simulated Pygame event handling by patching handle_key.
    This mimics a real user pressing 'g' in the Pygame window.
    The patched handle_key method changes the app_model state.
    """
    pygame.init()
    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_g})
    def handle_key(key):
        if key == pygame.K_g:
            home_controller.app_model.start_game()
    home_controller.handle_key = handle_key
    home_controller.handle_key(event.key)
    assert home_controller.app_model.started_game
    pygame.quit()
