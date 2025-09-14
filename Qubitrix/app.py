"""
Qubitrix MVC entry point and orchestration.
Run this file to launch the MVC version of Qubitrix.
"""

from Qubitrix.model import GameModel
from Qubitrix.view import GameView
from Qubitrix.controller import GameController


def main():
    # Initialize MVC components
    model = GameModel()
    view = GameView(model)
    controller = GameController(model, view)

    # Start the game loop
    controller.run()


if __name__ == "__main__":
    main()
