file = input("Enter the file name: ")
part =  file.split(".")
if len(part) > 1:
    print("the file extension is: " , part[-1])
else:
    print("There is no extension")
