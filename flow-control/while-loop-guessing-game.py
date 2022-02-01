import random
highest = 10
answer = random.randint(1, highest)
print(answer)
guess_count = 0
guess = print(
    f"Please guess a number between 1 to {highest}. At anytime, you can enter 0 to exit\n")
while(guess != answer):
    guess = int(input())
    if guess == 0:
        print("You are exiting the game")
        break
    elif guess == answer and guess_count == 0:
        print("Well done, you got it first time")
        break
    else:
        guess_count += 1
        if guess < answer:
            print("Please guess higher")
        elif guess > answer:
            print("Please guess lower")
        elif guess == answer:
            print("Well done, you guessed it")
            break

# version 2 simple
