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

    def handle_command(self, cmd):
        if cmd == 'h':
            self.app_model.go_home()
        elif cmd == 'g':
            self.app_model.start_game()
        elif cmd == 'p':
            if self.app_model.current_view == ViewType.GAME:
                self.app_model.pause_game()
            else:
                print("[AppController] Pause only allowed during game.")
        elif cmd == 'r':
            if self.app_model.current_view == ViewType.PAUSE:
                self.app_model.resume_game()
            else:
                print("[AppController] Resume only allowed from pause.")
        elif cmd == 's':
            self.app_model.show_summary()
        elif cmd == 't':
            self.app_model.show_settings()
        elif cmd == 'q':
            print("Quitting.")
            return False
        else:
            print("Unknown command. [h=home, g=game, p=pause, r=resume, s=summary, t=settings, q=quit]")
        return True

    def run(self):
        print("Qubitrix MVC Demo. Press h=home, g=game, p=pause, r=resume, s=summary, t=settings, q=quit.")
        while True:
            view = self.app_view.get_view(self.app_model.current_view)
            if view is not None:
                view.render()
            else:
                print(f"[ERROR] No view for {self.app_model.current_view}")
            cmd = input("Command: ").strip().lower()
            if not self.handle_command(cmd):
                break
