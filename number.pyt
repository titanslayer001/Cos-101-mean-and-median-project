# numbers.py
from collections import Counter

def sum_of_list(numbers):
    """1. Return the sum of a list of numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

def average_of_list(numbers):
    """2. Return the average / mean of a list of numbers"""
    if len(numbers) == 0:
        return 0
    return sum_of_list(numbers) / len(numbers)

def median_and_mode(numbers):
    """3. Return the median and mode of a list of numbers"""
    if len(numbers) == 0:
        return None, None

    # MEDIAN
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    middle = n // 2
    if n % 2 == 1:
        median = sorted_nums[middle]
    else:
        median = (sorted_nums[middle - 1] + sorted_nums[middle]) / 2

    # MODE - the number that appears most
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]

    # If all appear once, no mode
    if max_count == 1:
        mode = "No mode - all numbers appear once"
    elif len(modes) == 1:
        mode = modes[0]
    else:
        mode = modes

    return median, mode

# This part lets you test it alone
if __name__ == "__main__":
    test = [10, 20, 20, 30, 40, 50]
    print("List:", test)
    
print("Sum:", sum_of_list(test))
print("Average:", average_of_list(test))
print("Median and Mode:", median_and_mode(test))
