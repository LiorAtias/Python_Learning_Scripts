# name = input("Please enter your name: ")
# if age >= 18:
#    print("You are old enough to vote!")

# elif age == 900:
#    print("Sorry, Yoda, you die in return of the jedi")

# else:
#    print("Please come back in {0} years".format(18 - age))

# for i in range(1, 13):
#    print("No. {} and squared is {} and cubed is {} and fourth is {} and fifth is {} and sixth {}".format(i, i ** 2, i ** 3, i ** 4, i ** 5, i ** 6))
#    print("*" * 105)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print("{}, your age is" .format(name) ,age)

if age < 18:
    print("Please come back in {0} years".format(18 - age))

elif age == 900:
    print("Sorry, Yoda, you die in return of the jedi")
    
else:
    print("You are old enough to vote!")

