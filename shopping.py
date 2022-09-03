shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
# excluding an item from the list using if statement
    if item != "spam":
        print("Buy " + item)
print("***********************")
for item in shopping_list:
    if item == "rice":
        continue

    print("Buy " + item)
