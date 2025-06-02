number = int(input("Enter a number to see its multiplication table:"))
for n in range(1,11):
    multiple = number * n
    print(f"{number} * {n} = {multiple}")
