parrot = "Norwegian Blue"
print(
    parrot
    + "\n"
    + parrot[3]
    + "\n"
    + parrot[4]
    + "\n"
    + parrot[9]
    + "\n"
    + parrot[3]
    + "\n"
    + parrot[6]
    + "\n"
    + parrot[8]
    + "\n"
)

print(parrot[-1])  # this prints from the end of the string
print(parrot[-2])
print(parrot[-14])


print(
    parrot
    + "\n"
    + parrot[-11]
    + "\n"
    + parrot[-10]
    + "\n"
    + parrot[-5]
    + "\n"
    + parrot[-11]
    + "\n"
    + parrot[-8]
    + "\n"
    + parrot[-6]
    + "\n"
)

print("Slicing the string")
print(parrot[0:6])  # slice the string from 0 to 5
print(parrot[3:5])
print(parrot[10:14])

print(parrot[0:6:2])

print("backward Slicing the string")
#                    1         2
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]

# doesn't print letter 'a' as the stop value is at 0(zero) which is not included
print(backwards)

backwards_new = letters[25::-1]
print(backwards_new)

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:17:-1])
