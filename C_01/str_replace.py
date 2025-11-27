s = input("enter the string: ")
first = s[0]
modified = s.replace(first, 's')
result = first + modified[1:]
print("result:", result)
