import random # importing the random module

highest = 1000 # sn integer that specify the highest number in the guessing game
answer = random.randint(1, highest) # using a random number in the range of 1-10
# print(answer) # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer: # this is the loop generator enables the user guessings
    guess = int(input())

    if guess == 0: # this line enables a get away from the game
        break
    if guess == answer:
        print("Well done, you guessed it!")
        print("you guessed it in {} tries".format(guess))
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
#        guess = int(input())
#        if guess == answer:
#            print("Well done, you guessed it!")
#        else:   # guess must be lower than answer
#            print("sorry, you have not guessed it correctly")    










# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed it correctly")
# else:
#     print("You got it the first time!")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")