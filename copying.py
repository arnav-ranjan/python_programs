import copy

org = [1, 2, 3, 4, 5, 6]

cpy = copy.copy(org)

cpy[0] = -10

print(org)
print(cpy)