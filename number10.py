def classify_numbers(numbers):
    # Initialize counts
    counts = {"positive": 0, "zero": 0, "negative": 0}
    
    # Loop through each number
    for num in numbers:
        if num > 0:
            print(f"{num} is positive")
            counts["positive"] += 1
        elif num == 0:
            print(f"{num} is zero")
            counts["zero"] += 1
        else:
            print(f"{num} is negative")
            counts["negative"] += 1
    
    # Return the counts dictionary
    return counts

# Example usage:
nums = [10, -5, 0, 23, -1, 0, 7]
result = classify_numbers(nums)
print("\nCounts:", result)
