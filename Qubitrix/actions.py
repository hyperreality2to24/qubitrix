from enum import Enum, auto

class Action(Enum):
    MOVE_LEFT = auto()
    MOVE_RIGHT = auto()
    MOVE_FWD = auto()         # Move piece forward in depth
    MOVE_BWD = auto()       # Move piece backward in depth
    SOFT_DROP = auto()
    HARD_DROP = auto()
    ROTATE_X_CW = auto()     # Rotate around X axis clockwise
    ROTATE_X_CCW = auto()    # Rotate around X axis counterclockwise
    ROTATE_Y_CW = auto()     # Rotate around Y axis clockwise
    ROTATE_Y_CCW = auto()    # Rotate around Y axis counterclockwise
    ROTATE_Z_CW = auto()     # Rotate around Z axis clockwise
    ROTATE_Z_CCW = auto()    # Rotate around Z axis counterclockwise
    HOLD = auto()
    PAUSE = auto()
    QUIT = auto()
    CAMERA_ROTATE_LEFT = auto()
    CAMERA_ROTATE_RIGHT = auto()