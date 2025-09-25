class SummaryView:
    def render(self, screen):
        import pygame
        font = pygame.font.SysFont(None, 48)
        text = font.render("Summary Screen", True, (255, 255, 255))
        screen.blit(text, (20, 20))
