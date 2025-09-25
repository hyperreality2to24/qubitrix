import pytest
from Qubitrix.model.grid3d import Grid3D

def test_grid3d_init_and_get_set():
	grid = Grid3D(3, 3, 3, default=0)
	assert grid.get(0, 0, 0) == 0
	grid.set(1, 1, 1, 5)
	assert grid.get(1, 1, 1) == 5
	assert grid.get(2, 2, 2) == 0

def test_clear_plane():
	grid = Grid3D(2, 2, 2, default=0)
	grid.set(0, 0, 1, 7)
	grid.set(1, 1, 1, 8)
	grid.clear_plane(1)
	assert grid.get(0, 0, 1) == 0
	assert grid.get(1, 1, 1) == 0

def test_is_plane_full():
	grid = Grid3D(2, 2, 2, default=0)
	for x in range(2):
		for y in range(2):
			grid.set(x, y, 1, 1)
	assert grid.is_plane_full(1)
	grid.set(0, 0, 1, 0)
	assert not grid.is_plane_full(1)

def test_remove_plane_and_shift_down():
	grid = Grid3D(2, 2, 3, default=0)
	# Fill z=2 with 2s, z=1 with 1s, z=0 with 0s
	for x in range(2):
		for y in range(2):
			grid.set(x, y, 2, 2)
			grid.set(x, y, 1, 1)
	grid.remove_plane_and_shift_down(1)
	# z=1 should now be all 0s, z=2 should be all 2s
	for x in range(2):
		for y in range(2):
			assert grid.get(x, y, 1) == 0
			assert grid.get(x, y, 2) == 2
# moved from tests/test_grid3d.py
