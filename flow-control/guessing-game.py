answer = 5

print("Please guess a number between 1 to 10:")
guess = int(input())
if guess > 10 or guess < 0:
    print(
        f"You were asked to enter a number between 1 to 10 but you entered {guess}")
elif guess < answer:
    print(f"Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > answer:
    print(f"Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")
