class PauseModel:
    """
    Stores the bitmap of the paused screen for display in PauseView.
    """
    def __init__(self, paused_bitmap=None):
        self.paused_bitmap = paused_bitmap
