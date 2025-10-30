names = input( "Enter first names separated by space: ").split()
count = 0
for name in names:
    
    count = count + name.lower().count('a')
print("total number of 'a' in the list: ", count)
