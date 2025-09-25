
import pygame

class SettingsScreenController:
    """
    Handles input and logic for the Settings screen.
    """
    def __init__(self, view):
        self.view = view

    def handle_input(self, cmd):
        print(f"[SettingsScreenController] Received command: {cmd}")

    def render(self):
        self.view.render()

    @staticmethod
    def run_pygame(view):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Qubitrix - Settings Screen")
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            screen.fill((50, 50, 50))
            view.render(screen)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
