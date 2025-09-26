import pygame
import math

class Grid3DView:
    def __init__(self, grid_model, rotation_angle):
        self.grid_model = grid_model
        self.rotation_angle = rotation_angle

    def render(self, screen):
        WIDTH = self.grid_model.width
        DEPTH = self.grid_model.depth
        HEIGHT = self.grid_model.height
        angle = self.rotation_angle

        # Match the grid area in GameView
        grid_w, grid_h = 320, 320
        grid_x = 120
        grid_y = 100
        scale_x = grid_w / WIDTH
        scale_y = grid_h / HEIGHT
        center_x = grid_x + grid_w // 2
        center_y = grid_y + grid_h // 2

        # --- Draw grid frame sensitive to orientation ---
        corners = []
        for x, y in [(0,0), (WIDTH-1,0), (WIDTH-1,DEPTH-1), (0,DEPTH-1)]:
            rx = x - (WIDTH-1)/2
            ry = y - (DEPTH-1)/2
            rz = 0
            tx = rx * math.cos(angle) - ry * math.sin(angle)
            ty = ry * math.cos(angle) + rx * math.sin(angle)
            screen_x = center_x + tx * scale_x
            screen_y = center_y + ty * scale_x - rz * scale_y
            corners.append((screen_x, screen_y))
        pygame.draw.lines(screen, (80, 80, 200), True, corners, 4)

        # --- Draw cubes from grid ---
        for x in range(WIDTH):
            for y in range(DEPTH):
                for z in range(HEIGHT):
                    cube_id = self.grid_model.get(x, y, z)
                    if cube_id > 0:
                        rx = x - (WIDTH-1)/2
                        ry = y - (DEPTH-1)/2
                        rz = z
                        tx = rx * math.cos(angle) - ry * math.sin(angle)
                        ty = ry * math.cos(angle) + rx * math.sin(angle)
                        screen_x = center_x + tx * scale_x
                        screen_y = center_y + ty * scale_x - rz * scale_y
                        color = (200, 200, 200)
                        pygame.draw.rect(screen, color, (screen_x-10, screen_y-10, 20, 20))

        # --- Draw current piece ---
        # If the grid model has a reference to the game model, try to draw the current piece
        game_model = getattr(self.grid_model, 'game_model', None)
        if game_model and hasattr(game_model, 'current_piece') and game_model.current_piece:
            piece = game_model.current_piece
            piece_id = piece.get('id', 9)
            for cube in piece.get('cubes', []):
                x, y, z = cube
                rx = x - (WIDTH-1)/2
                ry = y - (DEPTH-1)/2
                rz = z
                tx = rx * math.cos(angle) - ry * math.sin(angle)
                ty = ry * math.cos(angle) + rx * math.sin(angle)
                screen_x = center_x + tx * scale_x
                screen_y = center_y + ty * scale_x - rz * scale_y
                color = (220, 120, 40)
                pygame.draw.rect(screen, color, (screen_x-10, screen_y-10, 20, 20))
