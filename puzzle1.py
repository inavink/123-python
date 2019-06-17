print("Welcome!!")
g = 0
while g!=5:
    g = int(input("Guess the number "))
    if g==5:
        print("You Won!!")
    else:
        if (g > 5) and (g <= 10):
            print("you are very close")
        elif g > 10:
            print("Too high")
        else: 
                print("Too low")
        print("You lose!!")
print("Game Over")
