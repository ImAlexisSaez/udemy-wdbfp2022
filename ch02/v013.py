friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# local_friends = {"Rolf"}
local_friends = friends.difference(abroad)
print(local_friends)

# Cuidado con el orden
local_friends = abroad.difference(friends)
print(local_friends)  # Empty set, set()

total_friends = friends.union(abroad)
print(total_friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

art_only = art.difference(science)
print(art_only)
science_only = science.difference(art)
print(science_only)
both_subjects = art.intersection(science)
print(both_subjects)
