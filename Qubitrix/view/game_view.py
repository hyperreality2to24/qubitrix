class GameView:
    def __init__(self, model=None):
        self.model = model

    def render(self):
        print("[VIEW] GameView: Game screen")
        if self.model:
            print(f"  Level: {getattr(self.model, 'level', 'N/A')}")
            print(f"  Score: {getattr(self.model, 'score', 'N/A')}")
            print(f"  Current Piece: {getattr(self.model, 'current_piece', 'N/A')}")
        else:
            print("  [No game model attached]")
