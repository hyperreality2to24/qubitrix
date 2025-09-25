from Qubitrix.view.base_view import BaseView

class GameView(BaseView):
    def __init__(self, model=None):
        super().__init__()
        self.model = model

    def render(self, screen):
        import pygame
        # Title bar
        self.draw_text(screen, "QUBITRIX", (screen.get_width() // 2 - 120, 20))

        # Grid area (center)
        grid_w, grid_h = 320, 320
        grid_x = 120
        grid_y = 100
        pygame.draw.rect(screen, (80, 80, 80), (grid_x, grid_y, grid_w, grid_h), 2)
        self.draw_text(screen, "[Grid will appear here]", (grid_x + 40, grid_y + grid_h // 2 - 20))

        # Next shapes and speed multiplier (right of grid)
        next_x = grid_x + grid_w + 40
        next_y = grid_y
        self.draw_text(screen, "Next Shapes:", (next_x, next_y))
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

