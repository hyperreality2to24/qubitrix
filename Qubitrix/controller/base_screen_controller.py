import pygame

class BaseScreenController:
    """
    Base class for all screen controllers. Handles common Pygame event loop logic, including quitting on 'q' or window close.
    Subclasses should override handle_key and optionally render_screen.
    """
    def __init__(self, view, app_model=None):
        self.view = view
        self.app_model = app_model or getattr(view, 'app_model', None)

    def run_pygame(self):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption(self.get_caption())
        clock = pygame.time.Clock()
        running = True
        quit_requested = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    quit_requested = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        quit_requested = True
                    else:
                        self.handle_key(event.key)
            self.render_screen(screen)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        if quit_requested:
            return 'quit'

    def handle_key(self, key):
        """
        Override in subclass to handle keys other than 'q'.
        """
        pass

    def render_screen(self, screen):
        """
        Override in subclass for custom rendering.
        """
        screen.fill((0, 0, 0))
        if hasattr(self.view, 'render_pygame'):
            self.view.render_pygame(screen)
        elif hasattr(self.view, 'render'):
            self.view.render()

    def get_caption(self):
        """
        Override in subclass for custom window caption.
        """
        return "Qubitrix Screen"
