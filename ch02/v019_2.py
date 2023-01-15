friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

starts_s = [name for name in friends if name.startswith("S")]
print(starts_s)

friends_s = ["Sam", "Samantha", "Saurabh"]
print(friends_s is starts_s)  # False
print(friends_s[0] is starts_s[0])  # True

# Different id
print(f"friends_s id: {id(friends_s)}\nstarts_s id: {id(starts_s)}")

# Para que sean iguales
friends_s = starts_s
print(friends_s is starts_s)
print(friends_s[0] is starts_s[0])
print(f"friends_s id: {id(friends_s)}\nstarts_s id: {id(starts_s)}")
