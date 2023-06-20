"""
(ITERATIVE APPROACH)
Algorithm:
The merge_sort function takes an array arr as input.
If the length of the array is less than or equal to 1, it is considered already sorted and returned as is.
The initial step involves splitting the array into individual subarrays, each containing a single element.
The algorithm then iteratively merges adjacent subarrays until only one subarray remains.
In each iteration, the merge function is called to merge pairs of adjacent subarrays into a single sorted subarray.
The merged subarrays are stored in a new list.
This process continues until only one subarray remains, which is the sorted array.
The sorted array is then printed as output.
"""
def merge_sort(arr):
    """
    Sorts an array using the iterative Merge Sort algorithm.
    """
    if len(arr) <= 1:
        return arr

    # Split the array into subarrays of size 1
    subarrays = [[val] for val in arr]

    # Merge subarrays iteratively until only one subarray remains
    while len(subarrays) > 1:
        merged = []
        for i in range(0, len(subarrays), 2):
            left = subarrays[i]
            right = subarrays[i + 1] if i + 1 < len(subarrays) else []
            merged.append(merge(left, right))

        subarrays = merged

    return subarrays[0]

def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    """
    merged = []
    i = j = 0

    # Merge elements from left and right arrays in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements from left or right array, if any
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
"""
(Recursive)
Algorithm:
The merge_sort function takes an array arr as input.
If the length of the array is less than or equal to 1, it is considered already sorted and returned as is.
The array is divided into two halves, left and right, by finding the midpoint.
The merge_sort function is called recursively on the left and right halves to sort them separately.
Each recursive call further divides the subarrays until they reach a base case of length 1.
The merge function is then called to merge the sorted left and right halves into a single sorted array.
The merged array is returned as the result of the current recursive call.
The recursion continues until the original array is completely sorted.
The sorted array is then printed as output.
"""
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

# Example usage
numbers = [5, 3, 8, 2, 1]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)