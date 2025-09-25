import pygame # all views need to render into a pygame screen
class BaseView:
    """
    Base class for all Qubitrix views.
    Provides shared font setup and a utility method for drawing text.
    Subclasses should override the render(screen) method.
    """
    def __init__(self):
        if not pygame.font.get_init():
            pygame.font.init()
        self.font = pygame.font.SysFont(None, 48)
        self.text_color = (255, 255, 255)

    def draw_text(self, screen, text, pos):
        label = self.font.render(text, True, self.text_color)
        screen.blit(label, pos)

    def render(self, screen):
        raise NotImplementedError("Subclasses must implement render(screen)")
