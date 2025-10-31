import math
start = int(input("enter starting range"))
end = int(input("enter ending range"))
result = []
for num in range (start, end+1):
    if 100<= num <=9999:
        if all(int(digit) % 2==0 for digit in str(num)):
            root = int(math.sqrt(num))
            if root * root == num:
                result.append(num)
print("FOUR DIGIT NUMBERS WITH ALL EVEN DIGITS AND PERFECT SQAURE ARE: ")
print(result)
