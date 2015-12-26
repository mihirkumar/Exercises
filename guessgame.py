#Game of guessing a number between 1 and 20

import random
number = random.randint(1,20)
print ("The number is between 1 and 20")
guessed = False

while guessed == False:
	print ("Take a guess")
	guess = int(input())

	if guess < number:
		print("Your guess is too low")
	elif guess > number:
		print("Your guess is too high")
	elif guess == number:
		print("Your guess is right! The number is " + str(number) + "!")
		guessed = 
		True

		