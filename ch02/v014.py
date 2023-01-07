# Comparaciones: ==, !=, <, >, <=, >=
print(5 == 5)
print(5 > 5)
print(5 < 5)
print(5 != 6)

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)
print(friends is abroad)  # False: no están en el mismo espacio de memoria
# is: dice si exactamente dos elementos son iguales
print(friends is friends)