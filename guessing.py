#Write code that plays a number guessing game with the user. The code will loop until the user gets the number right or quits. Follow the directions below.

#    First, have your program generate a random integer between 1 and 20 (the "secret number").
#    Then prompt the user "Guess a number between 1 and 20 (enter 0 to quit): "
#    Read in their answer with raw_input() (recall that you'll need to convert the return value to an int) and save it in a variable
#    Compare their guess to your "secret number":
#        If the guess is correct, print "You got it!" and end the loop.
 #       If the guess is higher than the secret number, print "Too high!" and allow the user to keep guessing.
 #       If the guess is lower than the secret number, print "Too low!" and allow the user to keep guessing.
 #       If they entered 0, print "Ending program" and end the loop.



import random
import sys
num = random.randint(1,20)
guess = int(input("Guess a number between 1 and 20 (enter 0 to quit): "))
#print (num)
if guess == 0:
    print ("Ending program")
    sys.exit()
#elif guess == 0:
#    print ("Ending program")
while guess > num:
    print("Too high")
    guess = int(input("Guess again: "))
    if guess == 0:
        print ("Ending program")
        sys.exit()
while guess < num:
    print("Too low")
    guess = int(input("Guess again: "))
    if guess == 0:
        print ("Ending program")
        sys.exit()
if guess == num:
    print ("You got it")
