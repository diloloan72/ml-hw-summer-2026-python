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


def main():
    n = int(input("Enter N (positive integer): "))
    store = NumberStore()

    for i in range(1, n + 1):
        number = int(input(f"Enter number {i}: "))
        store.insert(number)

    x = int(input("Enter X: "))
    print(store.search(x))


if __name__ == "__main__":
    main()
