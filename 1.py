color_l1 = input("Enter colors for list 1 (separated by spaces): ").split()
color_l2 = input("Enter colors for list 2 (separated by spaces): ").split()
unique_colors = list(set(color_l1) - set(color_l2))
print("new list is", unique_colors)
