n = input("Enter the list of number with space in between: ")
numbers = n.split()
numbers = [int(n) for n in numbers]
total = sum(numbers)
print("sum of the list will be", total)
