from Qubitrix.model.app_model import AppModel, ViewType
from Qubitrix.view.app_view import AppView
from Qubitrix.controller.app_controller import AppController


class DummyView:
    def render(self):
        pass

class DummyAppView(AppView):
    """
    DummyAppView is used to isolate controller logic from real view rendering.
    It overrides get_view to always return a DummyView, so tests focus only on controller/model behavior.
    """
    def __init__(self, app_model):
        super().__init__(app_model)
    def get_view(self, view_type):
        return DummyView()


def test_pause_only_allowed_from_game(capsys):
    """
    Test that pause is only allowed from the GAME view.
    - If not in GAME, pause should do nothing.
    - If in GAME, pause should transition to PAUSE.

    capsys is used to suppress and capture output from the controller (e.g., error messages),
    so the test output remains clean and we can focus on state changes.
    """
    app_model = AppModel()
    app_view = DummyAppView(app_model)
    controller = AppController(app_model, app_view)
    # Simulate pause command from HOME
    app_model.current_view = ViewType.HOME
    controller.run = lambda: None  # Disable main loop
    controller.app_model.current_view = ViewType.HOME
    with capsys.disabled():
        controller.handle_command('p')
        assert app_model.current_view == ViewType.HOME

    # Now from GAME
    controller.app_model.current_view = ViewType.GAME
    with capsys.disabled():
        controller.handle_command('p')
        assert app_model.current_view == ViewType.PAUSE


def test_resume_only_allowed_from_pause(capsys):
    """
    Test that resume is only allowed from the PAUSE view.
    - If not in PAUSE, resume should do nothing.
    - If in PAUSE, resume should transition to GAME.

    capsys is used to suppress and capture output from the controller (e.g., error messages),
    so the test output remains clean and we can focus on state changes.
    """
    app_model = AppModel()
    app_view = DummyAppView(app_model)
    controller = AppController(app_model, app_view)
    controller.run = lambda: None
    # Not from PAUSE
    controller.app_model.current_view = ViewType.GAME
    with capsys.disabled():
        controller.handle_command('r')
        assert app_model.current_view == ViewType.GAME
    # From PAUSE
    controller.app_model.current_view = ViewType.PAUSE
    with capsys.disabled():
        controller.handle_command('r')
        assert app_model.current_view == ViewType.GAME
    # From PAUSE
    controller.app_model.current_view = ViewType.PAUSE
    with capsys.disabled():
        controller.handle_command('r')
        assert app_model.current_view == ViewType.GAME
