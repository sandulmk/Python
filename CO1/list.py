numbers = input("Enter a list numbers: ")
numbers=[int(x) for x in numbers.split()]
result = []
for num in numbers:
    if num > 100:
        result.append('over')
    else:
            result.append(num)
print("Modified List: ", result)
