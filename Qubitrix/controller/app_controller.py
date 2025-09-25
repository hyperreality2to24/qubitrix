
from Qubitrix.model.app_model import AppModel, ViewType
from Qubitrix.view.app_view import AppView
from Qubitrix.controller.game_screen_controller import GameScreenController
from Qubitrix.controller.pause_screen_controller import PauseScreenController
from Qubitrix.controller.settings_screen_controller import SettingsScreenController

class AppController:
    """
    Top-level controller for the application. Manages the main loop and delegates to screen-specific controllers.
    """
    def __init__(self, app_model, app_view):
        self.app_model = app_model
        self.app_view = app_view
        self.quit_flag = False
        from Qubitrix.controller.home_screen_controller import HomeScreenController
        self.screen_controllers = {
            ViewType.HOME: lambda: HomeScreenController(self.app_view.get_view(ViewType.HOME)),
            ViewType.GAME: lambda: GameScreenController(self.app_model.game_model, self.app_view.get_view(ViewType.GAME)),
            ViewType.PAUSE: lambda: PauseScreenController(self.app_view.get_view(ViewType.PAUSE)),
            ViewType.SETTINGS: lambda: SettingsScreenController(self.app_view.get_view(ViewType.SETTINGS)),
            # Add more as needed
        }

    def handle_command(self, cmd):
        # Delegate to the current screen controller if available
        controller = self.get_screen_controller()
        if controller:
            controller.handle_input(cmd)

        # App-level commands (navigation, quit, etc.)
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

    def get_screen_controller(self):
        factory = self.screen_controllers.get(self.app_model.current_view)
        if factory:
            return factory()
        return None

    def run(self):
        print("Qubitrix MVC Demo. Press h=home, g=game, p=pause, r=resume, s=summary, t=settings, q=quit.")
        while not self.quit_flag:
            controller = self.get_screen_controller()
            # Use Pygame event loop for each screen if available
            if self.app_model.current_view == ViewType.HOME and controller:
                from Qubitrix.controller.home_screen_controller import HomeScreenController
                # Pass quit_flag by reference
                if HomeScreenController.run_pygame(self.app_view.get_view(ViewType.HOME)) == 'quit':
                    self.quit_flag = True
                    break
            elif self.app_model.current_view == ViewType.GAME and controller:
                GameScreenController.run_pygame(self.app_model.game_model, self.app_view.get_view(ViewType.GAME))
            elif self.app_model.current_view == ViewType.PAUSE and controller:
                PauseScreenController.run_pygame(self.app_view.get_view(ViewType.PAUSE))
            elif self.app_model.current_view == ViewType.SETTINGS and controller:
                SettingsScreenController.run_pygame(self.app_view.get_view(ViewType.SETTINGS))
            else:
                view = self.app_view.get_view(self.app_model.current_view)
                if view is not None:
                    view.render()
                else:
                    print(f"[ERROR] No view for {self.app_model.current_view}")
                cmd = input("Command: ").strip().lower()
                if not self.handle_command(cmd):
                    break

            # After returning from a Pygame screen, immediately launch the next screen if current_view changed to another Pygame screen
            while self.app_model.current_view in (ViewType.HOME, ViewType.GAME, ViewType.PAUSE, ViewType.SETTINGS) and not self.quit_flag:
                controller = self.get_screen_controller()
                if self.app_model.current_view == ViewType.HOME and controller:
                    from Qubitrix.controller.home_screen_controller import HomeScreenController
                    if HomeScreenController.run_pygame(self.app_view.get_view(ViewType.HOME)) == 'quit':
                        self.quit_flag = True
                        break
                elif self.app_model.current_view == ViewType.GAME and controller:
                    GameScreenController.run_pygame(self.app_model.game_model, self.app_view.get_view(ViewType.GAME))
                elif self.app_model.current_view == ViewType.PAUSE and controller:
                    PauseScreenController.run_pygame(self.app_view.get_view(ViewType.PAUSE))
                elif self.app_model.current_view == ViewType.SETTINGS and controller:
                    SettingsScreenController.run_pygame(self.app_view.get_view(ViewType.SETTINGS))
                else:
                    break
