import pygame
from Qubitrix.model.app_model import ViewType

class HomeScreenController:
    """
    Handles input and logic for the Home screen, using Pygame for input and rendering.
    """
    def __init__(self, view):
        self.view = view
        self.app_model = getattr(view, 'app_model', None)

    @staticmethod
    def run_pygame(view):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Qubitrix - Home Screen")
        clock = pygame.time.Clock()
        running = True
        app_model = getattr(view, 'app_model', None)
        quit_requested = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    if app_model:
                        app_model.current_view = ViewType.HOME
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        running = False
                        if app_model:
                            app_model.start_game()
                    elif event.key == pygame.K_q:
                        running = False
                        quit_requested = True
            screen.fill((50, 50, 50))
            # view.render_pygame(screen)  # Implement in HomeView if needed
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        if quit_requested:
            return 'quit'
