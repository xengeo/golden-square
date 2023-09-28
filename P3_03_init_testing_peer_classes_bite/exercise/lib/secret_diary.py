# File: lib/secret_diary.py

class SecretDiary:
    def __init__(self, diary):
        self._secret_diary = diary
        self._is_locked = True

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        if self._is_locked:
            raise Exception("Go away!")
        else:
            return self._secret_diary.read()

    def lock(self):
        # Locks the diary
        # Returns nothing
        self._is_locked = True

    def unlock(self):
        # Unlocks the diary
        # Returns nothing
        self._is_locked = False