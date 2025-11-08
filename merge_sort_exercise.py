def merge_sort(L):
    pass
    ## Divide: Divide the n-element sequence to be 
    #   sorted into two subsequences of n/2 elements each.
    
    ## Conquer: Sort the two subsequences recursively 
    #   using merge sort.

    ## Combine: Merge the two sorted subsequences to 
    #   produce the sorted answer.


# Example usage:
my_list = [12, 11, 13, 5, 6, 7]
my_list_sorted = merge_sort(my_list)
assert my_list_sorted == sorted(my_list)

# Example usage:
my_list = list(reversed(range(10**8)))
my_list_sorted = merge_sort(my_list)
assert my_list_sorted == sorted(my_list)