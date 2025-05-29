# Original tuple of student marks
marks = (65, 70, 75, 80, 85)

# I. Print the first and last elements of the tuple
print("First mark:", marks[0])
print("Last mark:", marks[-1])

# II. Unpack the tuple elements into separate variables
m1, m2, m3, m4, m5 = marks
print("Unpacked marks:", m1, m2, m3, m4, m5)

# III. Create a new tuple by adding 5 marks to each element
new_marks = tuple(mark + 5 for mark in marks)

# IV. Print both the original and the new tuples
print("Original marks tuple:", marks)
print("Updated marks tuple (+5):", new_marks)
