class GameController:
    """
    Handles user input and orchestrates communication between the model and view.
    """
    def __init__(self, model, view):
        import pygame
        from Qubitrix.controller.grid_controller import GridController
        from Qubitrix.controllers.abstract_controller import GameEvent
        self.model = model
        self.view = view
        self.grid_controller = GridController(model.grid, model)
        self.event_queue = []
        self.GameEvent = GameEvent
        # Key mapping from monolithic app
        self.key_map = {
            pygame.K_d: self.GameEvent.MOVE_PIECE_RIGHT,
            pygame.K_w: self.GameEvent.MOVE_PIECE_FORWARD,
            pygame.K_a: self.GameEvent.MOVE_PIECE_LEFT,
            pygame.K_s: self.GameEvent.MOVE_PIECE_BACKWARD,
            pygame.K_k: self.GameEvent.ROTATE_GRID_CLOCKWISE,
            pygame.K_l: self.GameEvent.ROTATE_GRID_COUNTERCLOCKWISE,
            pygame.K_SPACE: self.GameEvent.LOWER_PIECE,
            pygame.K_LSHIFT: self.GameEvent.HOLD_PIECE,
            pygame.K_SEMICOLON: self.GameEvent.PAUSE_GAME,
            pygame.K_ESCAPE: self.GameEvent.QUIT_GAME,
        }

    def run(self):
        import pygame
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if (game_event := self.key_map.get(event.key)):
                        self.event_queue.append(game_event)
            # Process event queue
            while self.event_queue:
                evt = self.event_queue.pop(0)
                self.handle_game_event(evt)
            self.view.render()

    def handle_game_event(self, event):
        # Example: delegate to grid controller
        if event == self.GameEvent.LOWER_PIECE:
            self.grid_controller.place_piece(self.model.current_piece, keystroke=event)
        elif event == self.GameEvent.PAUSE_GAME:
            self.model.mode = "Paused"
        elif event == self.GameEvent.QUIT_GAME:
            self.model.mode = "Home"
        # Add more event handling as needed
