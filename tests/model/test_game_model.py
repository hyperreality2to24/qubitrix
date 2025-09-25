import pytest
from Qubitrix.model.game_model import GameModel
from Qubitrix.model.grid3d import Grid3D

def test_initial_state():
	model = GameModel()
	assert model.grid is None
	assert model.mode == "Home"
	assert model.score == 0
	assert model.level == model.initial_level
	assert model.score_multiplier == 1.0
	assert isinstance(model.key_hold_times, list)

def test_init_game_sets_grid():
	model = GameModel()
	model.init_game()
	assert isinstance(model.grid, Grid3D)
	assert model.mode == "Playing"
	assert model.score == 0
	assert model.level == model.initial_level
# moved from tests/test_game_model.py
