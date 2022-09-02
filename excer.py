parrot = "Norwegian Blue"

print(parrot)
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])


print(parrot)
print(parrot[2:5])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print((parrot[3:5]), parrot[-11]+parrot[-8]+parrot[-6])

print(parrot[:])

print(parrot[-2])

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1] # reverse the sequemce
print(backwards)

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])


print(letters[-1:])

print(letters[0])