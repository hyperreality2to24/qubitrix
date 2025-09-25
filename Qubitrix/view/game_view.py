class GameView:
    def __init__(self, model=None):
        self.model = model

    def render(self, screen):
        import pygame
        font = pygame.font.SysFont(None, 48)
        text = font.render("Game Screen", True, (255, 255, 255))
        screen.blit(text, (20, 20))
