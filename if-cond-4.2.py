''' Write a program that prompts a user to enter two integer values.
Print the message 'Equal' if both the entered values are equal.'''
print("Enter a number here ")
a=int(input())
print("Enter the second number")
b=int(input())
if a == b:
    print("a is equal to b")
else:
    print("Both numbers are different")