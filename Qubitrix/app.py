
"""
Qubitrix MVC entry point and orchestration.
Run this file to launch the MVC version of Qubitrix.
"""


from Qubitrix.model.app_model import AppModel, ViewType
from Qubitrix.view.app_view import AppView
from Qubitrix.controller.app_controller import AppController

def main():
    app_model = AppModel()
    app_view = AppView(app_model)
    app_controller = AppController(app_model, app_view)
    app_controller.run()

if __name__ == "__main__":
    main()
