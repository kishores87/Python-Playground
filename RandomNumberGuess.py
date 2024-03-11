import random
import math

print("I'll pick a random number and you've to guess.... To start, enter the lower and upper bound numbers")


lower = int(input("Enter lower bound number: "))
upper = int(input("Enter upper bound number: "))

x= random.randint(lower, upper)

print ("You have only", upper-lower, "chances to guess")
count=0
while count < upper-lower:
    count += 1

    guess = int(input ("Type your guess :"))

    if x == guess:
        print("Congratulations!! You guessed the number in", count , "attempt")
        break
    elif guess > x:
        print("You guessed high number..Try again")
    elif guess < x:
        print("You guessed too small..Try again")
if count>= upper-lower:
    print("Game is over. The number is", x,  "Sorry, You did not guess the number in", upper-lower, "attempt. Better luck next time")