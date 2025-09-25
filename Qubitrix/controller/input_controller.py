from collections import deque
from Qubitrix.actions import Action

class InputController:
    """
    Maps user input (keyboard, pygame events, etc.) to game Actions and queues them for the model.
    """
    def __init__(self):
        self.action_queue = deque()
        # Example: key-to-action mapping (can be extended)
        self.key_map = {
            'left': Action.MOVE_LEFT,
            'right': Action.MOVE_RIGHT,
            'up': Action.MOVE_FWD,
            'down': Action.MOVE_BWD,
            'space': Action.HARD_DROP,
            'z': Action.ROTATE_Z_CCW,
            'x': Action.ROTATE_Z_CW,
            'a': Action.ROTATE_X_CCW,
            'd': Action.ROTATE_X_CW,
            'w': Action.ROTATE_Y_CCW,
            's': Action.ROTATE_Y_CW,
            'c': Action.HOLD,
            'p': Action.PAUSE,
            'q': Action.QUIT,
        }

    def map_input(self, input_event):
        """
        Map a raw input (string or event) to an Action and queue it.
        """
        action = self.key_map.get(input_event)
        if action:
            self.action_queue.append(action)

    def get_next_action(self):
        """
        Retrieve the next queued Action, or None if queue is empty.
        """
        if self.action_queue:
            return self.action_queue.popleft()
        return None

    def clear_actions(self):
        self.action_queue.clear()

# Example usage:
# controller = InputController()
# controller.map_input('left')
# action = controller.get_next_action()
# if action:
#     model.handle_action(action)
