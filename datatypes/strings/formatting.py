print("Left alignement")
for i in range(1, 13):
    # print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))  # the ouput is not formatted with this
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(
        i, i**2, i**3))  # the ouput is not formatted with this

print()
print("Right alignement")

for i in range(1, 13):
    # print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))  # the ouput is not formatted with this
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(
        i, i**2, i**3))  # the ouput is not formatted with this

print()
print("Center alignement")

for i in range(1, 13):
    # print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))  # the ouput is not formatted with this
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(
        i, i**2, i**3))  # the ouput is not formatted with this

print()
print("Fill with space")

for i in range(1, 13):
    # print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))  # the ouput is not formatted with this
    print("No. {0:2} squared is {1: <3} and cubed is {2: <4}".format(
        i, i**2, i**3))  # the ouput is not formatted with this

print()
print("format with f")
print("Pi is approximatley {0:12}".format(22/7))
print("Pi is approximatley {0:12f}".format(22/7))
print("Pi is approximatley {0:12.50f}".format(22/7))
print("Pi is approximatley {0:52.50f}".format(22/7))
print("Pi is approximatley {0:62.50f}".format(22/7))
print("Pi is approximatley {0:72.50f}".format(22/7))

print()
print("Pyhton 3.6 string formatting")

age = 24
print(f"I\'m {age} years old")
print(f"Pi is approximately {22/7:12.50f}")

meal1 = "spam"+"eggs"+"beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
egs
beans"""

print(meal1)
print(meal2)
print(meal3)
print(meal4)
