import unittest

from exercises.exercise_6_door_controller_with_locking.door_controller import DoorController, DoorLockedError


class TestDoorController:

    def setup_method(self) -> None:
        self.door_controller = DoorController()

    def test_initially_door_is_not_opened(self):
        pass

    def test_open_door_opens(self):
        pass

    def test_close_door_after_open_door(self):
        # opening door
        self.door_controller.open()
        # closing door
        self.door_controller.close()
        # test if door opened

    def test_initially_door_is_not_locked(self):
        # sprawdzić czy początkowo drzwi nie są zablokowane
        pass

    def test_lock_door_closes_and_locks(self):
        # wazne aby pamietac ze drzwi najpierw musza byc otwarte!!!
        # testujemy czy drzwi po lock() są zamkniete i zablokowane
        # opening
        pass

    def test_unlock_door(self):
        # aby można było odblokowac drzwi muszą byc one najpierw zablokowane!!!
        # closing
        pass

    def test_exception_on_opening_locked_doors(self):
        # Testujemy wystąpienie wyjątku. Polecam sprawdzić w prezentacji składnię!
        # Użyć rozwiązania z context managerem 'with'
        # Pamietaj ze trzeba zaimportowac wyjatek DoorLockedError
        # Pamietajmy ze najpierw musimy zablokowac drzwi, a potem dopiero probowac je otwierac
       pass
