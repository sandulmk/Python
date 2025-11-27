list1 = [int(x) for x in input("enter numbers for first list: ").split()]
list2 = [int(x) for x in input("enter numbers for first list: ").split()]
if len(list1)== len(list2):
    print("equal")
else:
        print("different")
if sum(list1)==sum(list2):
    print("sum is equal")
else:
        print("sum is different")

common = set(list1) & set(list2)
if common:
    print("common value")
else:
    print("no common value")
