if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you a person with no name?")
