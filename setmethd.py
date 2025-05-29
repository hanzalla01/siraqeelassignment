my_set = {1, 2, 3, 4} # Initial set
# 1. add() – Add a single element to the set
my_set.add(5)
print("After add(5):", my_set)  # Output: {1, 2, 3, 4, 5}
# 2. update() – Add multiple elements at once
my_set.update([6, 7])
print("After update([6, 7]):", my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}
# 3. remove() – Remove a specific element
my_set.remove(2)
print("After remove(2):", my_set)  # Output: {1, 3, 4, 5, 6, 7}
# 4. union() and | – Combine sets
a = {1, 2, 3}
b = {3, 4, 5}
print("Union using union():", a.union(b))  # Output: {1, 2, 3, 4, 5}
print("Union using |:", a | b)             # Same output
# 5. intersection() and & – Common items
print("Intersection using intersection():", a.intersection(b))  # Output: {3}
print("Intersection using &:", a & b)                           # Same output
