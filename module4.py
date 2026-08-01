# The program asks the user for input N (positive integer) and reads it
# Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
# In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.

n = int(input("Enter N (positive integer): "))

numbers = []
for i in range(n):
    value = int(input(f"Enter number {i + 1}: "))
    numbers.append(value)

x = int(input("Enter X (integer to search for): "))

result = -1
for i in range(n):
    if numbers[i] == x:
        result = i + 1  
        break

print(result)
