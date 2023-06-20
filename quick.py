"""
Algorithm:
The quick_sort function takes an array arr as input.
If the length of the array is less than or equal to 1, it is considered already sorted and returned as is.
The algorithm chooses a pivot element from the array. In this implementation, the pivot is selected as the middle element.
The array is then partitioned into three sub-arrays: elements less than the pivot, elements equal to the pivot, and elements greater than the pivot.
The sub-arrays are created using list comprehensions.
The quick_sort function is recursively called on the left and right sub-arrays.
The sorted sub-arrays are concatenated with the middle elements to form the final sorted array.
The recursion continues until the original ar
"""
def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm.
    """
    if len(arr) <= 1:
        return arr

    # Choose a pivot element
    pivot = arr[len(arr) // 2]

    # Partition the array into two sub-arrays around the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the sub-arrays
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
