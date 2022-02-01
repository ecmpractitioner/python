string1 = "India is"
string2 = "a beautiful"
string3 = "country"
string4 = "with plenty of"
string5 = "natural resources"
# this adds space between words
print(string1, string2, string3, string4, string5)
# this doesn't add space between words
print(string1 + string2 + string3 + string4 + string5)

# mutlipily strings
print("Hello " * 5)

# check if a string exists in given string
print()
print("check if a string exists in given string")
today = "Friday"
print("Fri" in today)
print("day" in today)
print("Thur" in today)

print()
print("formatting string")
age = 24
print("My age is " + str(age) + " years")  # this is in python 2

print("My age is {0} years".format(age))  # this is in python 3

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(
    31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nove:{1}, Dec: {2}".format(28, 30, 31))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nove:{1}
Dec: {2}""".format(28, 30, 31))  # use triple quotes to span the text in multiple lines

print("""This is done
using
tripple quotes""")

print()
