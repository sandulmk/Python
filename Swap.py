s1 = input("Enter a name: ")
s2 = input("Enter another name: ")
n_s1 = s2[1] + s1[1:] if len(s1) > 1 else s2[1]
n_s2 = s1[1] + s2[1:] if len(s2) > 1 else s1[1]
result = n_s1 + " " + n_s2
print(result)
