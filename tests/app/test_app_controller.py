import pytest
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

def test_pause_only_allowed_from_game():
	"""
	Test that pause is only allowed from the GAME view.
	- If not in GAME, pause should do nothing.
	- If in GAME, pause should transition to PAUSE.
	"""
	app_model = AppModel()
	app_view = DummyAppView(app_model)
	controller = AppController(app_model, app_view)
	controller.run = lambda: None  # Disable main loop
	# Simulate pause command from HOME
	app_model.current_view = ViewType.HOME
	controller.handle_command('p')
	assert app_model.current_view == ViewType.HOME
	# Now from GAME
	app_model.current_view = ViewType.GAME
	controller.handle_command('p')
	assert app_model.current_view == ViewType.PAUSE

def test_resume_only_allowed_from_pause():
	"""
	Test that resume is only allowed from the PAUSE view.
	- If not in PAUSE, resume should do nothing.
	- If in PAUSE, resume should transition to GAME.
	"""
	app_model = AppModel()
	app_view = DummyAppView(app_model)
	controller = AppController(app_model, app_view)
	controller.run = lambda: None
	# Not from PAUSE
	app_model.current_view = ViewType.GAME
	controller.handle_command('r')
	assert app_model.current_view == ViewType.GAME
	# From PAUSE
	app_model.current_view = ViewType.PAUSE
	controller.handle_command('r')
	assert app_model.current_view == ViewType.GAME
