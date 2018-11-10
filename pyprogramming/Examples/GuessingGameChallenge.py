from random import randint

randNum = randint(1,101)
print ('Random Number: {}'.format(randNum))

noOfGuesses = 0
userInput = []

while True:
    userInput.append(int(input('Enter a number: ')))
    if (userInput[noOfGuesses] == 999):
        print ('Thanks for having fun!')
        break
    elif (userInput[noOfGuesses] == randNum):
        print ('\nPERFECT!! You guessed it in {} attempts'.format(noOfGuesses+1))
        break
    elif ((userInput[noOfGuesses] < 1) or (userInput[noOfGuesses] > 100)):
        print ('OUT OF BOUNDS')
    elif (abs(userInput[noOfGuesses] - randNum) <= 10):
        if (noOfGuesses == 0):
            print ("WARM!")
        else:
            print ('WARMER!')
    else:
        if (noOfGuesses == 0):
            print ('COLD!')
        else:
            print ('COLDER!')
    noOfGuesses += 1

print ('\nHere is the list of guesses you have made')
print (userInput)
