# time complexity O(n2)
# We start by traversing through each element in the array.
# In each iteration, we compare adjacent elements in the array.
# If the elements are in the wrong order (smaller element comes after the larger element), we swap them.
# This process is repeated until the largest element "bubbles" up to its correct position at the end of the array.
# After the first iteration, the largest element is guaranteed to be in its correct position at the end of the array.
# We repeat steps 2-5 for the remaining unsorted portion of the array until the entire array is sorted.
# def bubble_sort(arr):
    # Traverse through each element in the array
    
        # Last i elements are already in place, so we can ignore them in the inner loop
        
            # Compare adjacent elements
            
                # Swap the elements if they are in the wrong order
                

# Test the bubble sort algorithm
array = 
print("Original array:", array)
bubble_sort(array)
print("Sorted array:", array)
