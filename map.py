def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)



nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())

salaries = list(map(lambda x: x+bonus, salaries))

print(salaries)
