## Author: Feras Isied
## Description: Generate a number between 1 and 100 including both values 1 and 100
##  and compare it to user input.

# Import randint()
from random import randint

# Function for comparing userInput and randNumber
def randomNumberGuess():
    userInput = int(input("Enter a number between 1 and 100!\n"))
    randNumber = randint(1,100) # rand number between 1 and 100
    numberOfTries = 1 # counter for number of tries

    #while (userInput != randNumber): 
    while (numberOfTries != 8 and userInput != randNumber): # loop while number of tries !=8
        userInput = int(input("Try again. Enter a number between 1 and 100!\n"))
        if (userInput < randNumber):
            print("The number you guessed is too low! Try again.")
        elif (userInput > randNumber):
            print("The number you guessed is too high! Try again.")

        numberOfTries += 1
        if (numberOfTries == 8):
            print("You have exceeded the number of tries, which is 8 tries. Try again later!")
            quit() # quit the program

    if (userInput == randNumber):
        print("Congrats, you guessed the random number which is " + str(randNumber) + "!")
randomNumberGuess()