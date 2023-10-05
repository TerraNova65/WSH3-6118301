def serial_sum(start, end=None):
    if end is None:
        end = start
    total = 0
    for number in range(start, end + 1):
        total += number
    return total

# Example usage
result1 = serial_sum(4)
result2 = serial_sum(2, 4)

# Print the results
print(f"Sum of numbers from 1 to 4: {result1}")
print(f"Sum of numbers from 2 to 4: {result2}")