low = int(input("Please enter the lowest number \n"))
high = int(input("Please enter the highest number \n"))
print(f"Please think of a number between {low} and {high}")
print("Press ENTER to start")

guesses = 1

while True:
    guess = low+(high-low)//2
    high_low = input(
        f"My guess is {guess}. Should I guess higher or lower? Enter h or l, or c if my guess was correct \n").casefold()
    if high_low == "h":
        low = guess+1
    elif high_low == 'l':
        high = guess-1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses")
        break
    else:
        print("Please enter h or l or c")
        guesses += 1
