from Qubitrix.model.app_model import AppModel, ViewType
from Qubitrix.view.app_view import AppView

class AppController:
    """
    Top-level controller for the application. Manages the main loop and delegates to screen-specific controllers.
    """
    def __init__(self, app_model, app_view):
        self.app_model = app_model
        self.app_view = app_view
        # You can add a mapping of ViewType to controller here if needed

    def run(self):
        print("Qubitrix MVC Demo. Press h=home, g=game, p=pause, r=resume, s=summary, t=settings, q=quit.")
        while True:
            view = self.app_view.get_view(self.app_model.current_view)
            if view is not None:
                view.render()
            else:
                print(f"[ERROR] No view for {self.app_model.current_view}")
            cmd = input("Command: ").strip().lower()
            if cmd == 'h':
                self.app_model.go_home()
            elif cmd == 'g':
                self.app_model.start_game()
            elif cmd == 'p':
                self.app_model.pause_game()
            elif cmd == 'r':
                self.app_model.resume_game()
            elif cmd == 's':
                self.app_model.show_summary()
            elif cmd == 't':
                self.app_model.show_settings()
            elif cmd == 'q':
                print("Quitting.")
                break
            else:
                print("Unknown command. [h=home, g=game, p=pause, r=resume, s=summary, t=settings, q=quit]")
