shopping_list = ["milk", "pasta", "egga", "spam", "bread", 'rice']

print("using continue")

for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)

item_to_find = "spam3"
found_at = None  # None is a cnstant that accounts to nothing

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index

if found_at is not None:
    print(f"{item_to_find} was found at position {found_at}")
else:
    print(f"{item_to_find} was not found")
