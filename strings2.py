# extracting seperators from an string object
number = "9,223;372:036 854,775;807"
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)