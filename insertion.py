"""
Algorithm:
The insertion_sort function takes an array arr as input.
It starts by setting the length of the array to n.
The algorithm traverses through the array from index 1 to n-1.
For each element at index i, it is compared with the elements before it, starting from index i-1 and moving towards index 0.
If an element is greater than the current element key, it is shifted one position to the right.
This process continues until the element key is inserted at the correct position in the sorted subarray.
The sorted array is then printed as output.
"""
def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.
    """
    n = len(arr)

    # Traverse through 1 to n
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted at the right position

        # Move elements of arr[0...i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array:", arr)
