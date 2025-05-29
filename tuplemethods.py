# 1. Accessing Tuple Items
my_tuple = (10, 20, 30, 40, 50)
print("Accessing first item:", my_tuple[0])      # Output: 10
print("Accessing last item:", my_tuple[-1])      # Output: 50
# 2. Looping Through a Tuple
print("\nLooping through tuple:")
for item in my_tuple:
    print(item)
# 3. Joining Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2
print("\nJoined tuple:", joined_tuple)           # Output: (1, 2, 3, 4, 5, 6)
# 4. Updating a Tuple (Convert to list, modify, convert back)
temp_list = list(my_tuple)
temp_list[1] = 25  # Change the second element
updated_tuple = tuple(temp_list)
print("Updated tuple (via list):", updated_tuple)  # Output: (10, 25, 30, 40, 50)
# 5. Unpacking a Tuple
a, b, c, d, e = my_tuple
print("\nUnpacked values:", a, b, c, d, e)
# 6. Tuple Method: count()
sample_tuple = (1, 2, 3, 2, 4, 2)
count_2 = sample_tuple.count(2)
print("\nCount of 2 in sample_tuple:", count_2)   # Output: 3
# 7. Tuple Method: index()
index_of_3 = sample_tuple.index(3)
print("Index of 3 in sample_tuple:", index_of_3)  # Output: 2