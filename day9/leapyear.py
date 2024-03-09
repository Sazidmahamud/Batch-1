year=int(input("input a year:"))
if year%400==0:
    print(f"{year}is a leap year.")
elif year%100==0:
    print(f"{year}is a not leap year.")
elif year% 4==0:
    print(f"{year}is a leap year.")
else:
   print(f"(is not a leap year.")
    
