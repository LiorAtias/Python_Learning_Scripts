# adventure game base structure
available_exits = ["north", "south", "east", "west"]

# chosen_exit = "" (**this is another option for using None value***) 
chosen_exit = None
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit": # .casefold is written to ensure lowercase input from the user
        print("Game over!")
        break

print("aren't you glad you got out of there")