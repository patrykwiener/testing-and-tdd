"""
DOOR CONTROLLER WITH LOCKING

Na podstawie wczesniej stworzonej klasy DoorController stworzymy mechanizm ryglowania drzwi.

W przypadku próby otwarcia drzwi zaryglowanych rzucany jest wyjatek DoorLockedError.
"""


class DoorLockedError(Exception):
    pass


class DoorController:

    def __init__(self):
        self._is_opened = False
        self._is_locked = False

    def is_door_opened(self):
        return self._is_opened

    def is_door_locked(self):
        pass

    def open(self):
        self._is_opened = True

    def close(self):
        self._is_opened = False

    def lock(self):
        pass

    def unlock(self):
        pass
