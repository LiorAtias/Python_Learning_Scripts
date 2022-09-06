low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guess = 1
while True:
    guess = low + (high -low) // 2
    high_low = input("My guess is {}. should I guess higher or lower? "
    "Enter h or l or c if my guess is correct"
    .format(guess)).casefold()