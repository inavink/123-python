# To check number is prime or number
x=int(input("Enter the number "))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
