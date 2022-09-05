# searching for item that does not exist in the list
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "albatros" # change values between spam and albatros to see the difference
found_at = None

# for index in range (6) 0-5:
# for index in range(len(shopping_list)):
#    if shopping_list[index] == item_to_find:
#        found_at = index
#        break # bacuse when we found the item, there's no need to keep on the search
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("the word {} is not found in the list".format(item_to_find))