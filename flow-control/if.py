from time import process_time_ns


# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

# if age >= 18:
#     #print("Congrajulations {0}, you are old enought to vote".format(name))
#     print(f"Congrajulations {name}, you are old enough to vote ")
#     print("Please put an X in the box")
# else:
#     print(f"{name}, you have to wait for {18-age} more years before you can vote")

# print()
# print("using elif")

# name = input("Please enter your name: \n")
# age = int(input(f"How old are you, {name}?\n"))

# if age < 18:
#     print(f"{name}, you have to wait for {18-age} more years before you can vote")
# elif age >= 18 and age < 900:
#     print(f"Congrajulations, {name}. You are old enough to vote")
# else:
#     print("How come you are still alive???")

answer = 5

print("Please guess a number between 1 to 10:")
guess = int(input())
if guess > 10 or guess < 0:
    print(
        f"You were asked to enter a number between 1 to 10 but you entered {guess}")
elif guess < answer:
    print(f"Please guess higher")
elif guess > answer:
    print(f"Please guess lower")
else:
    print("You got it first time")
