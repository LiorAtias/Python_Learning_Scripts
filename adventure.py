# adventure game base structure
available_exits = ["north", "south", "east", "west"]

# chosen_exit = "" (**this is another option for using None value***) 
chosen_exit = None
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")

print("aren't you glad you got out of there")