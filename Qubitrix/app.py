
"""
Qubitrix MVC entry point and orchestration.
Run this file to launch the MVC version of Qubitrix.
"""

from Qubitrix.model.app_model import AppModel, ViewType
from Qubitrix.view.app_view import AppView

def main():
    app_model = AppModel()
    app_view = AppView(app_model)
    print("Qubitrix MVC Demo. Press h=home, g=game, p=pause, r=resume, s=summary, t=settings, q=quit.")
    while True:
        view = app_view.get_view(app_model.current_view)
        if view is not None:
            view.render()
        else:
            print(f"[ERROR] No view for {app_model.current_view}")
        cmd = input("Command: ").strip().lower()
        if cmd == 'h':
            app_model.go_home()
        elif cmd == 'g':
            app_model.start_game()
        elif cmd == 'p':
            app_model.pause_game()
        elif cmd == 'r':
            app_model.resume_game()
        elif cmd == 's':
            app_model.show_summary()
        elif cmd == 't':
            app_model.show_settings()
        elif cmd == 'q':
            print("Quitting.")
            break
        else:
            print("Unknown command. [h=home, g=game, p=pause, r=resume, s=summary, t=settings, q=quit]")

if __name__ == "__main__":
    main()
