my_list = []

my_list.append(10)
my_list.append(5)
my_list.append(8)
print("After append:", my_list)  # Output: [10, 5, 8]
# 2. insert() - Insert item at specific index
my_list.insert(1, 15)  # Insert 15 at index 1
print("After insert:", my_list)  # Output: [10, 15, 5, 8]
# 3. remove() - Remove the first occurrence of a specified value
my_list.remove(5)
print("After remove:", my_list)  # Output: [10, 15, 8]
# 4. pop() - Remove and return item
last_item = my_list.pop()  # Removes last item (8)
print("After pop():", my_list)  # Output: [10, 15]
print("Popped item:", last_item)  # Output: 8
# pop at specific index
first_item = my_list.pop(0)  # Removes item at index 0 (10)
print("After pop(0):", my_list)  # Output: [15]
print("Popped item at index 0:", first_item)  # Output: 10
# 5. sort() - Sort the list in ascending order
my_list.append(20)
my_list.append(3)
my_list.append(7)
print("Before sort:", my_list)  # Output: [15, 20, 3, 7
my_list.sort()
print("After sort:", my_list)  # Output: [3, 7, 15, 20]