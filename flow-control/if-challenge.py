name = input("Please enter your name: \n")
age = int(input("Please enter your age: \n"))

if 18 <= age < 31:
    print(f"Hey {name}, welcome to the holiday")
else:
    print(
        f"We are extremly sorry {name}. Due to age restrictions, you are not allowed in this tour")
