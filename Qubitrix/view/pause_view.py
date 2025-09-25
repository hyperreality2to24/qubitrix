from Qubitrix.view.base_view import BaseView

import pygame
from Qubitrix.view.base_view import BaseView

class PauseView(BaseView):
    def __init__(self, app_model=None, pause_model=None):
        super().__init__()
        self.app_model = app_model
        self.pause_model = pause_model  # Should be a PauseModel instance

    def render(self, screen):
        # Blit the paused bitmap as background if available
        if self.pause_model and self.pause_model.paused_bitmap:
            screen.blit(self.pause_model.paused_bitmap, (0, 0))
        else:
            screen.fill((30, 30, 30))

        # Draw semi-transparent red rectangle overlay
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        rect_width, rect_height = 400, 120
        rect_x = (screen.get_width() - rect_width) // 2
        rect_y = (screen.get_height() - rect_height) // 2
        overlay.fill((0, 0, 0, 0))
        pygame.draw.rect(overlay, (255, 0, 0, 180), (rect_x, rect_y, rect_width, rect_height))
        screen.blit(overlay, (0, 0))

        # Draw "PAUSED" text in red, centered in the rectangle
        font = pygame.font.SysFont(None, 72)
        paused_text = font.render("PAUSED", True, (255, 0, 0))
        text_rect = paused_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(paused_text, text_rect)