numbers = [5, 12, 7, 18, 9, 24, 3, 16, 11]

# Counters
div_by_3_count = 0
even_not_div3_count = 0
odd_not_div3_count = 0

for x in numbers:
    if x % 3 == 0:
        print(f"{x} is divisible by 3")
        div_by_3_count += 1
    elif x % 2 == 0:
        print(f"{x} is even but not divisible by 3")
        even_not_div3_count += 1
    else:
        print(f"{x} is odd and not divisible by 3")
        odd_not_div3_count += 1

print("\nSummary:")
print(f"Numbers divisible by 3: {div_by_3_count}")
print(f"Numbers even but not divisible by 3: {even_not_div3_count}")
print(f"Numbers odd and not divisible by 3: {odd_not_div3_count}")
