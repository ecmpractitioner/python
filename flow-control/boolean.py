day = "Monday"
temperature = 30
raining = True

if (day == "Saturday" and temperature > 27) and not raining:
    print("Go swimming")
else:
    print("Stay home and learn python")

name = input("Please enter your name\n")

if name:
    print(f"Hello, {name}")
else:
    print("Are you the person with no name?")

print()
print("Use of in or not in")

parraot = "Norwegian Blue"

letter = input("Enter character: \n")

if letter in parraot:
    print(f"{letter} is in {parraot}")
else:
    print("I don't need that letter")

activity = input("what would you like to do today?\n")
if "cinema" not in activity.casefold():  # casefold converts to lowercase and also handles differetn char sets. Better use this instead of lowercase()
    print("I want to go to cinema")
