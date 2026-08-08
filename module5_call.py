from module5_mod import NumberStore


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
