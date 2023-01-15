grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

# total = sum(grades)  # Alternativa

average = total / amount
print(average)
