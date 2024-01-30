contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

x = input()

for name, age in contacts:
    if name == x:
        print(f"{x} is {age}")
        break

else:
    print("Not Found")


