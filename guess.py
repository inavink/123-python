print ("Welcome")
g = input ("Guess the number :")
guess = int(g)
if guess==5:
	print ("You Win!")
else:
	print ("You Lose! Try Again!!")
	if guess > 5:
		print ("Input number is higher than accurate number")
	else:
		print ("Input number is lower than accurate number")
print ("Game Over")


