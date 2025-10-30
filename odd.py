user_input = input("Enter integers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("List after removing even numbers:", odd_numbers)
