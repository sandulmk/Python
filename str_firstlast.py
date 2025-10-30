s = input("enter a string: ")
if len(s)>1:
    new_string = s[-1] + s[1:-1] + s[0]
else:
    new_string = 5
print("result is: ", new_string)
