numbers = [1, 3, 5]

doubled = []
for num in numbers:
    doubled.append(num * 2)

print(doubled)

# Alternativa: list comprehensions
doubled = [x * 2 for x in numbers]
print(doubled)
