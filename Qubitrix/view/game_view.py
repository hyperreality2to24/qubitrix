class GameView:
    """
    Responsible for rendering the game and UI (MVC version).
    """
    def __init__(self, model):
        self.model = model

    def render(self):
        # Render the game state
        print("[MVC] Rendering game token...")
        print("Game state:", self.model.get_token())
