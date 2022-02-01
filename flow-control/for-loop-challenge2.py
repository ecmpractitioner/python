for i in range(0, 100):
    if(i % 7 == 0):
        print(i)

print()
print("differetn way of doing")
for i in range(0, 100, 7):
    print(i)

print()
print("differetn way of doing")
for i in range(101)[::7]:
    print(i)
