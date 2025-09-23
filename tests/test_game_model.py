import pytest
from Qubitrix.model.game_model import GameModel

def test_initial_state():
    model = GameModel()
    assert model.mode == "Home"
    assert model.score == 0
    assert model.level == model.initial_level
    assert model.score_multiplier == 1.0
    assert isinstance(model.key_hold_times, list)
    assert model.grid is None

def test_init_game_sets_grid():
    model = GameModel()
    model.init_game()
    assert model.grid is not None
    assert model.mode == "Playing"
    assert model.score == 0
    assert model.level == model.initial_level

# Add more tests for piece management, scoring, etc. as migration continues
