activity = str(input("What would you like to do today? "))


if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
else:
    print("Great, lets go together!")