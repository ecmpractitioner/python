i = 0
while(i < 10):
    print(f"i is now {i}")
    i += 1

exits = ["north", "south", "east", "west"]
choosen_exit = ""
while choosen_exit not in exits:
    choosen_exit = input("Please choose the exit \n")

print("Finally, you made it through")
