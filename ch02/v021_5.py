# Separar una lista en dos
head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)  # No hace falta poner el *. Si se pone, es otra cosa.

*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)