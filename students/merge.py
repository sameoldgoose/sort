# time complexity T(n) = 2T(n/2) + O(n)
# Recursive Merge Sort:
# The merge_sort_recursive() function is the main function that performs the recursive merge sort.
# It checks the base case: if the array has only one element, it is already sorted, so it returns the array.
# Otherwise, it divides the array into two halves and recursively calls merge_sort_recursive() on each half.
# The merge() function is used to merge the sorted halves into a single sorted array.
# The merge() function compares elements from the left and right halves and merges them into a new list in sorted order.
# The merged list is returned to the previous recursive call until the entire array is sorted.
def merge_sort_recursive(arr):
    # Base case: if the array has only one element, it is already sorted
    

    # Divide the array into two halves
    
    # Recursively call merge_sort_recursive() on the two halves
    
    # Merge the sorted halves
    
# Iterative Merge Sort:

# The merge_sort_iterative() function performs the iterative merge sort.
# It starts by dividing the array into subarrays of size 1.
# It then merges the subarrays in a bottom-up manner, gradually increasing the subarray size.
# The merge() function is used to merge the subarrays, similar to the recursive version.
# The process continues until the subarray size is equal to the length of the array, resulting in a fully sorted array.

# time complexity O(n log n)
def merge(left, right):
    # Create an empty list to store the merged result
    
    # Compare elements from left and right halves and merge them
    
    # Append any remaining elements from the left and right halves
    
    # Return the merged result
    
# Test the recursive merge sort algorithm
array = ___
print("Original array:", array)
sorted_array = merge_sort_recursive(array)
print("Sorted array:", sorted_array)
