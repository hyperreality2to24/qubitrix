class Grid3D:
    """
    Declarative 3D grid for Qubitrix game state.
    Wraps a 3D list and provides clean access and utility methods.
    """
    def __init__(self, width, depth, height, default=0):
        self.width = width
        self.depth = depth
        self.height = height
        self.default = default
        self._grid = [[[default for _ in range(height)] for _ in range(depth)] for _ in range(width)]

    def get(self, x, y, z):
        return self._grid[x][y][z]

    def set(self, x, y, z, value):
        self._grid[x][y][z] = value

    def clear_plane(self, z):
        for x in range(self.width):
            for y in range(self.depth):
                self._grid[x][y][z] = self.default

    def is_plane_full(self, z):
        for x in range(self.width):
            for y in range(self.depth):
                if self._grid[x][y][z] == self.default:
                    return False
        return True

    def as_list(self):
        return self._grid

    def remove_plane_and_shift_down(self, z):
        """
        Remove the plane at height z, shift all planes above it down, and add a new empty plane at the top (z=0).
        """
        for x in range(self.width):
            for y in range(self.depth):
                for zz in range(z, 0, -1):
                    self._grid[x][y][zz] = self._grid[x][y][zz-1]
                self._grid[x][y][0] = self.default

    # Add more utility methods as needed
