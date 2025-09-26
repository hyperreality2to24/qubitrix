class GridController:
    """
    Handles all grid-specific logic: piece placement, collision, plane clearing, and grid state updates.
    """
    def __init__(self, grid_model, game_model=None):
        self.grid_model = grid_model
        self.game_model = game_model
        self.last_keystroke = None

    def place_piece(self, piece, keystroke=None):
        # Example: place piece cubes into the grid
        self.last_keystroke = keystroke
        for cube in piece.get('cubes', []):
            x, y, z = cube
            self.grid_model.set(x, y, z, piece.get('id', 9))

    def clear_full_planes(self):
        # Example: clear full planes in the grid
        cleared = 0
        for z in range(self.grid_model.height):
            if self.grid_model.is_plane_full(z):
                self.grid_model.clear_plane(z)
                cleared += 1
        return cleared

    def check_collision(self, piece):
        # Example: check if piece collides with grid
        for cube in piece.get('cubes', []):
            x, y, z = cube
            if self.grid_model.get(x, y, z) > 0:
                return True
        return False

    # Add more grid logic as needed (ghost piece, secluded spaces, etc.)
