# time complexity O(N^2)
# Algorithm
# We start by traversing through each element in the array, starting from the second element (index 1).
# For each element, we store it in a variable called key. This element will be inserted into the correct position in the sorted portion of the array.
# We compare the key with each element in the sorted portion of the array (elements before the key) from right to left.
# If an element is greater than the key, we shift that element one position to the right.
# We continue this process until we find the correct position for the key or reach the beginning of the array.
# Once we find the correct position, we insert the key into that position.
# We repeat steps 2-6 for each element in the array until the entire array is sorted.

def insertion_sort(arr):
    # Traverse through each element in the array starting from the second element
    
        # Store the current element to be inserted into the sorted portion of the array
        
        # Find the correct position to insert the current element in the sorted portion
        
        while j >= 0 and arr[j] > key:
            # Shift elements greater than the key to the right
            
        # Insert the key into its correct position(outside loop)
        

# Test the insertion sort algorithm
array = 
print("Original array:", array)
insertion_sort(array)
print("Sorted array:", array)