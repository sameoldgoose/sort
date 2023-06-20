# time complexity O (n*logn)
# Explanation of the quicksort algorithm:
# The quicksort algorithm follows the divide-and-conquer approach to sort an array.
# It selects a pivot element from the array (in this implementation, the last element).
# The array is then partitioned into three subarrays: elements smaller than the pivot, elements equal to the pivot, and elements greater than the pivot.
# Recursively, quicksort is called on the subarrays containing elements smaller and greater than the pivot.
# The base case is when the array has one or zero elements, in which case it is already sorted and returned.
# The sorted subarrays and the equal elements are combined to obtain the final sorted array.
def quick_sort(arr):
    # Base case: if the array has one or zero elements, it is already sorted
    

    # Select a pivot element (in this implementation, the last element)
    

    # Partition the array into two subarrays, elements smaller than the pivot and elements greater than the pivot
    left= []
    right = []
    equal = []
    

    # Recursively call quick_sort() on the subarrays
    

    # Combine the sorted subarrays and the equal elements
    

# Test the quicksort algorithm
array = __
print("Original array:", array)
sorted_array = quick_sort(array)
print("Sorted array:", sorted_array)
