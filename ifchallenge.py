name = str(input("Please enter your name: "))
age = int(input("Please enter yor age (in numbers only): "))
if age >= 18 and age < 31:
    print("HI {}, let's go to the vacation..".format(name))
else:
    print("Sorry {}, you are not in the proper age!".format(name))