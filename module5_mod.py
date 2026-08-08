class NumberStore:
    """Stores numbers and supports insertion and 1-based search."""

    def __init__(self):
        self._data = []

    def insert(self, value):
        self._data.append(value)

    def search(self, x):
        for index, value in enumerate(self._data, start=1):
            if value == x:
                return index
        return -1
