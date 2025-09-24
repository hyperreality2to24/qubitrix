import random
import math
from copy import deepcopy
from Qubitrix.model.grid3d import Grid3D

class GameModel:
    def __init__(self, app_model=None):
        self.app_model = app_model
        # Game state variables migrated from Game class
        self._mode = "Home"
        self.rotate_modifier = False
        self.key_hold_times = [0, 0, 0, 0, 0, 0, 0]
        self.initial_level = 1
        self._score = 0
        self.total_planes_cleared = 0
        self.plane_clear_level_progress = 0
        self.total_plane_clear_types = [0, 0, 0, 0]
        self.total_spin_clear_types = [0, 0, 0]
        self.total_spins = 0
        self.secluded_spaces = 0
        self._level = self.initial_level
        # ...initialize other fields as needed...
    # --- Properties for key state variables ---
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def current_piece(self):
        return self._current_piece

    @current_piece.setter
    def current_piece(self, value):
        self._current_piece = value

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, value):
        self._grid = value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    # Add more properties as needed for other state variables
    def score_mult_bonus(self, amount):
        from Qubitrix.qubitrix import MULT_BUFFER_SIZE
        self.score_mult_buffer += amount
        if self.score_mult_buffer > MULT_BUFFER_SIZE:
            self.score_multiplier += self.score_mult_buffer - MULT_BUFFER_SIZE
            self.score_mult_buffer = MULT_BUFFER_SIZE
            self.score_multiplier = min(self.score_multiplier, self.score_mult_cap)
        self.highest_score_multiplier = max(self.highest_score_multiplier, self.score_multiplier)

    def hold_piece(self):
        from Qubitrix.qubitrix import PIECES, Effects
        if not self.hold_piece_used:
            self.hold_piece_used = True
            if self.current_piece is None:
                return # Prevent error if hold is used before a piece is active
            current_piece_index = self.current_piece["id"] - 1
            self.current_piece, self.held_piece = self.held_piece, deepcopy(PIECES[current_piece_index])
            if not self.current_piece:
                self.load_upcoming_pieces()
                self.current_piece = deepcopy(self.next_pieces.pop(0))
            self.reset_piece_state()
            Effects().hold_piece.play(maxtime=300)

    def clear_planes(self):
        if not self.grid:
            return # Prevent error if clear_planes is called when game is not initialized
        from Qubitrix.qubitrix import HEIGHT, DEPTH, WIDTH, PLANE_CLEAR_SCORE_BONUSES, SPIN_CLEAR_SCORE_FACTOR, PLANE_CLEAR_MULT_BONUSES, SPIN_CLEAR_MULT_FACTOR, Effects
        planes_cleared = 0
        for z in range(HEIGHT):
            cubes = 0
            for y in range(DEPTH):
                for x in range(WIDTH):
                    if self.grid.get(x, y, z) > 0:
                        cubes += 1
            if cubes == DEPTH*WIDTH:
                planes_cleared += 1
                self.grid.remove_plane_and_shift_down(z)
        self.increase_score(PLANE_CLEAR_SCORE_BONUSES[min(planes_cleared, 4)] * (SPIN_CLEAR_SCORE_FACTOR if self.piece_spin_on_last_movement else 1))
        self.total_planes_cleared += planes_cleared
        self.plane_clear_level_progress += planes_cleared
        self.check_for_level_increase()
        self.score_mult_bonus(PLANE_CLEAR_MULT_BONUSES[min(planes_cleared, 4)] * (SPIN_CLEAR_MULT_FACTOR if self.piece_spin_on_last_movement else 1))
        if (planes_cleared > 0) and (type(planes_cleared) == int):
            if not self.piece_spin_on_last_movement:
                eval(f"Effects()['{min(planes_cleared, 4)}_plane_clear'].play(maxtime=1000)")
                self.total_plane_clear_types[min(planes_cleared, 4)-1] += 1
            else:
                eval(f"Effects()['{min(planes_cleared, 3)}_spin_clear'].play(maxtime=1000)")
                self.total_spin_clear_types[min(planes_cleared, 3)-1] += 1
        return planes_cleared

    # Continue migrating all other methods as needed...
    """
    Handles the game state and logic for Qubitrix (MVC version).
    """
    # --- End of __init__ ---

    # All field initializations should be in __init__ or init_game. No stray code here.

    def init_game(self):
        from Qubitrix.qubitrix import HEIGHT, DEPTH, WIDTH, get_level_requirement, PIECES, FPS, Effects
        self.grid = Grid3D(WIDTH, DEPTH, HEIGHT, default=0)
        self.mode = "Playing"
        self.score = 0
        self.total_planes_cleared = 0
        self.plane_clear_level_progress = get_level_requirement(self.initial_level-1)
        self.total_plane_clear_types = [0, 0, 0, 0]
        self.total_spin_clear_types = [0, 0, 0]
        self.total_spins = 0
        self.secluded_spaces = 0
        self.level = self.initial_level
        self.check_for_level_increase()
        self.score_multiplier = 1.0
        self.highest_score_multiplier = 1.0
        self.score_mult_buffer = 0.0
        self.score_mult_cap = 1.0 + self.level/5
        self.repeat_input_delay = FPS/7.5
        self.next_pieces = []
        self.get_new_piece()
        self.held_piece = {}
        self.grid_rotation = 0
        self.visual_grid_rotation = 0.0
        self.game_over_screen_time = 0

    def increase_score(self, points):
        self.score += points * self.score_multiplier

    def check_for_level_increase(self):
        from Qubitrix.qubitrix import get_level_requirement
        while self.plane_clear_level_progress >= get_level_requirement(self.level):
            self.level += 1

    def get_new_piece(self):
        from Qubitrix.qubitrix import PIECES
        self.load_upcoming_pieces()
        import copy
        self.current_piece = copy.deepcopy(self.next_pieces.pop(0))
        self.hold_piece_used = False
        self.get_secluded_spaces()
        self.reset_piece_state()

    def load_upcoming_pieces(self):
        from Qubitrix.qubitrix import PIECES, NEXT_PIECE_COUNT
        import random
        while len(self.next_pieces) <= NEXT_PIECE_COUNT:
            piece_bag = PIECES + [PIECES[random.randrange(0, 7)]]
            random.shuffle(piece_bag)
            self.next_pieces.extend(piece_bag)

    def reset_piece_state(self):
        self.tick_time = 0
        self.place_time = 0
        self.in_hard_drop = False
        if self.current_piece:
            self.lowest_center_elevation = self.current_piece["centers"][0][2]
            self.lowest_spin_elevation = self.current_piece["centers"][0][2]
        self.piece_spin_on_last_movement = False
        self.get_ghost_piece()

    def get_secluded_spaces(self):
        self.secluded_spaces = 0
        # ...existing code from Game.get_secluded_spaces() can be migrated here...

    def get_ghost_piece(self):
        import copy
        self.ghost_piece = copy.deepcopy(self.current_piece)
        # ...existing code from Game.get_ghost_piece() can be migrated here...

    # Add more migrated methods as needed from Game class

