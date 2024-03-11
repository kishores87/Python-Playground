import random
from collections import Counter


someWords = "apple banana mango strawberry"
someWords = someWords.split(' ')
word = random.choice(someWords)


if __name__ == "__main__":
    print('Guess the fruit name')

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        # flag is updated when the word is correctly guessed
        while (chances != 0) and flag == 0:
            print()
            chances -= 1
            try:
                guess = str(input('Enter a letter to guess'))
            except:
                print('Enter only a letter')
                continue

            #validation of guess
            if not guess.isalpha():
                print('Enter only Letter')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guess the letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range (k):
                    letterGuessed += guess
                    #The guess letter is added as many times as it occurs
            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print (char, end='')
                    correct += 1

                #if user has guessed all the letters
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is", end=' ')
                    print(word)
                    flag = 1
                    print("congratulations You won!")
                    break # break out of for loop
                    break # break out of while loop
            else:
                print('_', end=' ')

        # If user used all his chances
        if chances == 0 and (Counter(letterGuessed) != Counter(word)):
            print("You Lost! Try again..")
            print("The word was ", format(word))

    except KeyboardInterrupt:
        print("Bye! Try Again.")
        exit()
