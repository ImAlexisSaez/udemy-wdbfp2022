# String formatting

# f-strings in Python
name = "Bob"

print(f"Hello, {name}!")

name = "Rolf"

print(f"Hello, {name}!")

# Template strings with .format()
greeting = "Hello, {}!"  # Plantilla para saludar.
with_name = greeting.format(name)
with_name_two = greeting.format("Bob")

print(with_name)
print(with_name_two)

# Plantillas con más de un hueco
longer_phrase = "Hello, {}. Today is {}"

formatted = longer_phrase.format("Alexis", "saturday")

print(formatted)
