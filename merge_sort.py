def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the first half
        merge_sort(right_half)  # Recursively sort the second half

        # Merge the sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check for any remaining elements in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
my_list = list(range(10**7, 0, -1))  # A large list in reverse order

# calculate the time taken by merge_sort

import time
# start_time = time.time()
res = my_list.copy()
merge_sort(res)
# end_time = time.time()
# print(f"Time taken by merge_sort: {end_time - start_time} seconds")
# print("Sorted array is:", res)

# compare against the time taken by built-in sort
# start_time = time.time()
my_list.sort()
# end_time = time.time()
# print(f"Time taken by built-in sort: {end_time - start_time} seconds")
# print("Built-in sorted array is:", my_list)
assert res == my_list