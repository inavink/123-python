# Finding the Number of Days in a month
print("Enter the month (1-12)")
M=int(input())
if ((M > 0) & (M <=12)):
    if M==2:
        Year=int(input("Enter year (e.g. 2024)"))
        if ((Year %4==0) and (not(Year%100==0)) or (Year%400==0)):
            num_days = 29
            print("Number of days in Month ", M, "is ", num_days) 
        else:
            num_days = 28
            print("Number of days in Month ", M, "is ", num_days)    
    elif M in (1,3,5,7,8,12):
        num_days = 31
        print("Number of days in Month ", M, "is ", num_days)
    else:
        num_days = 30
        print("Number of days in Month ", M, "is ", num_days)
else: print("Please inter a valid number between 1-12")