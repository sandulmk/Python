current_year=int(input("Enter the current year: "))
final_year=int(input("Enter the final year: "))
print("Leap years between", current_year, "and", final_year, ":")
year=current_year
while year<=final_year:
    if(year%4==0 and year%100!=0) or (year%400==0):
        print(year)
    year+=1
