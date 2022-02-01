parraot = "Norwegian Blue"

for character in parraot:
    print(character)

number = "9,223;372:036 854,775:807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators += char
print(separators)

# print(char)
values = "".join(
    char if char not in separators else " " for char in number).split()

print(values)

print()

for i in range(1, 21):
    print(f"i is now {i}")


print()
print("Range with a step value")

for i in range(0, 10, 2):
    print(f"i is now {i}")

print()
print("Range with a -ve step value")

for i in range(10, 0, -2):
    print(f"i is now {i}")

age = 65
print()
if age in range(16, 66):
    print(f"Have a good day at work")

print()
print("Times table")

for i in range(1, 13):
    if i != 1:
        print(20*"*")
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
