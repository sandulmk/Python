user_input = input("Enter Some numbers: ")
numbers = user_input.split()
numbers = [int(n) for n in numbers]
positive_numbers =[]
for n in numbers:
    if n>0:
        positive_numbers.append(n)
print("positive numbers are: ", positive_numbers)
