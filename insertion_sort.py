def insertion_sort(arr):
    """
    Sorts a list using the insertion sort algorithm.

    Args:
        arr: The list to be sorted.

    Returns:
        The sorted list.
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted into the sorted part
        j = i - 1     # Index of the last element in the sorted part

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place the key in its correct position

    return arr

# Example usage:
my_list = [12, 11, 13, 5, 6]
sorted_list = insertion_sort(my_list.copy())
print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")