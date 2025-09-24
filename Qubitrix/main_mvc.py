"""
Entry point for the MVC version of Qubitrix. Wires up AppState, dummy views, and a simple controller loop to test view switching.
"""
from Qubitrix.model.app_state import AppState, ViewType
from Qubitrix.view.home_view import HomeView
from Qubitrix.view.game_view import GameView
from Qubitrix.view.pause_view import PauseView
from Qubitrix.view.summary_view import SummaryView
from Qubitrix.view.settings_view import SettingsView

VIEW_MAP = {
    ViewType.HOME: HomeView(),
    ViewType.GAME: GameView(),
    ViewType.PAUSE: PauseView(),
    ViewType.SUMMARY: SummaryView(),
    ViewType.SETTINGS: SettingsView(),
}

def main():
    app_state = AppState()
    print("Qubitrix MVC Demo. Press h=home, g=game, p=pause, r=resume, s=summary, t=settings, q=quit.")
    while True:
        view = VIEW_MAP[app_state.current_view]
        view.render()
        cmd = input("Command: ").strip().lower()
        if cmd == 'h':
            app_state.go_home()
        elif cmd == 'g':
            app_state.start_game()
        elif cmd == 'p':
            app_state.pause_game()
        elif cmd == 'r':
            app_state.resume_game()
        elif cmd == 's':
            app_state.show_summary()
        elif cmd == 't':
            app_state.show_settings()
        elif cmd == 'q':
            print("Quitting.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
