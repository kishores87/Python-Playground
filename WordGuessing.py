import random


name=input("Welcome!! Please enter your name: ")
print ("You've 12 chance to guess the fruit name.. Enter one character at a time.. Good luck", name)

fruitNames = ['apple', 'orange', 'pineapple', 'guava', 'tomato', 'banana']

randomWord=random.choice(fruitNames)
lenghtofRandomWord = len(randomWord)

guessCount=6
finalGuess= []

for x in range(lenghtofRandomWord):
    print("_")

while guessCount>0:
    inputChar=input("Guess the letter: ")
    print("Guessed char so far", finalGuess)

    if inputChar in randomWord and len(finalGuess) == 0:
        finalGuess.append(inputChar)
    elif inputChar in randomWord and len(finalGuess) > 0:
        if inputChar in finalGuess:
            print("checking if char exists", inputChar)
            if finalGuess.count(inputChar) >= randomWord.count(inputChar):
                print("This char is already guessed.. Try again!!")
                guessCount -= 1
                print("You have", guessCount, "more attempts to guess the word")
                if guessCount == 0:
                    print("You lose..")
                    print("The fruit name is", randomWord)

            else:
                print("This char is correct guess", inputChar)
                finalGuess.append(inputChar)
        else:
            print("This char is correct guess", inputChar)
            finalGuess.append(inputChar)

        if sorted(randomWord) == sorted(finalGuess):
            guessCount = 0
            print("You Win..")
            print("The fruit name is", randomWord)

    else:
        print("Wrong guess.. Try again!!")
        guessCount -= 1
        print("You have", guessCount, " more attempts to guess the word")
        if guessCount == 0:
            print("You lost..")
            print("The fruit name is", randomWord)