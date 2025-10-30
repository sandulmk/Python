data = {'apple': 3, 'banana': 1, 'cherry': 2}
values_asc = dict(sorted(data.items()))
values_desc = dict(sorted(data.items(),reverse=True))
print("dictionary is",data)
print("Ascending order",values_asc)
print("descending order",values_desc)
