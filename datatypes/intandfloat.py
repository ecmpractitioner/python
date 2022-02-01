print("In python 3, there is no limit to the int size unlike Java. Strange!!!")

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # integer division which truncates the floating point value
print(a % b)

print()

for i in range(
    1, a // b
):  # here if we use a/b, it throws an error because a/b produces a float point number which is 4.0 and same cannot be used as int
    print(i)
