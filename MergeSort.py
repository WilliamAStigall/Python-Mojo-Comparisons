import random
import time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

total_time = time.time()
# Example usage:
array = []
for i in range(1, 10001):  # Increase array size by one each time
    random_number = random.randint(0, 1000000)
    array.append(random_number)

    start_time = time.time()  # Start the timer

    sorted_array = merge_sort(array)

    end_time = time.time()  # Stop the timer
    execution_time = end_time - start_time

    print(f"Sorted array with size {i}")
    print(f"Execution time: {execution_time} seconds")

end_total = time.time()
program_time = end_total-total_time
print(f"Program execution time: {program_time} seconds")
