from Qubitrix.view.base_view import BaseView

class GameView(BaseView):
    def __init__(self, model=None):
        super().__init__()
        self.model = model

    def render(self, screen):
        import pygame
        import math
        from Qubitrix.view.grid3d_view import Grid3DView
        # Title bar
        self.draw_text(screen, "QUBITRIX", (screen.get_width() // 2 - 120, 20))

        # Grid area (center)
        grid_w, grid_h = 320, 320
        grid_x = 120
        grid_y = 100
        pygame.draw.rect(screen, (80, 80, 80), (grid_x, grid_y, grid_w, grid_h), 2)

        # Render the 3D grid using Grid3DView
        if self.model and getattr(self.model, 'grid', None) is not None and hasattr(self.model, 'visual_grid_rotation'):
            grid_model = self.model.grid
            rotation_angle = getattr(self.model, 'visual_grid_rotation', 0) * (math.pi / 2)
            grid_view = Grid3DView(grid_model, rotation_angle)
            grid_view.render(screen)
        else:
            self.draw_text(screen, "[Grid will appear here]", (grid_x + 40, grid_y + grid_h // 2 - 20))

        # Next shapes and speed multiplier (right of grid)
        next_x = grid_x + grid_w + 40
        next_y = grid_y
        self.draw_text(screen, "Next Shapes:", (next_x, next_y))
        # 3D project next piece queue using actual piece data and monolithic colors
        try:
            from Qubitrix.qubitrix import COLORS, CUBE_VERTEX_OFFSET
        except ImportError:
            COLORS = [(180, 180, 220)] * 10
            CUBE_VERTEX_OFFSET = 0.46
        if self.model and hasattr(self.model, 'next_pieces'):
            for i, piece in enumerate(self.model.next_pieces[:5]):
                base_x = next_x + 60
                base_y = next_y + 60 + i * 60
                piece_id = piece.get('id', 9)
                color = COLORS[piece_id]
                wire_color = tuple(max(0, int(c * 0.5)) for c in color)
                # 3D projection parameters
                rot = 0.5  # Slight angle for preview
                scale = 18
                offset_z = 0
                # Draw cubes
                for cube in piece.get('cubes', []):
                    x, y, z = cube
                    rx = x - 1.5
                    ry = y - 1.5
                    rz = z + offset_z + 4
                    tx = rx * math.cos(rot) - ry * math.sin(rot)
                    ty = ry * math.cos(rot) + rx * math.sin(rot)
                    draw_x = base_x + tx * scale
                    draw_y = base_y + ty * scale - rz * 6
                    pygame.draw.rect(screen, color, (draw_x-8, draw_y-8, 16, 16))
                    # Draw wireframe (darker)
                    pygame.draw.rect(screen, wire_color, (draw_x-8, draw_y-8, 16, 16), 2)
                self.draw_text(screen, f"Shape {i+1}", (next_x + 100, next_y + 50 + i * 60))
        else:
            for i in range(5):
                pygame.draw.rect(screen, (180, 180, 220), (next_x, next_y + 40 + i * 50, 40, 40), 2)
                self.draw_text(screen, f"Shape {i+1}", (next_x + 50, next_y + 50 + i * 50))
        self.draw_text(screen, "Speed Mult:", (next_x, next_y + 320))
        self.draw_text(screen, "x1.0", (next_x + 120, next_y + 320))

        # Statistics (far right)
        stats_x = next_x + 200
        stats_y = grid_y
        stats = [
            "Single clears:", "Double clears:", "Triple clears:", "Quad clears:",
            "Piece spins:", "Spin singles:", "Spin doubles:", "Spin triples:"
        ]
        self.draw_text(screen, "Statistics:", (stats_x, stats_y))
        for i, stat in enumerate(stats):
            self.draw_text(screen, f"{stat} 0", (stats_x, stats_y + 40 + i * 40))

        # Level and score (above grid)
        if self.model:
            self.draw_text(screen, f"Level: {getattr(self.model, 'level', 'N/A')}", (grid_x, grid_y - 60))
            self.draw_text(screen, f"Score: {getattr(self.model, 'score', 'N/A')}", (grid_x + 180, grid_y - 60))
        else:
            self.draw_text(screen, "No game model attached", (grid_x, grid_y - 60))

