"""
Algorithm:
The selection_sort function takes an array arr as input.
It starts by setting the length of the array to n.
The algorithm traverses through the array from the first element to the second-to-last element.
In each iteration, it finds the minimum element in the unsorted part of the array.
The minimum element's index is stored in min_index.
If the minimum element is found, it is swapped with the first element of the unsorted part.
This process continues until the array is completely sorted.
The sorted array is then printed as output.
"""

def selection_sort(arr):
    """
    Sorts an array using the Selection Sort algorithm.
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array:", arr)
