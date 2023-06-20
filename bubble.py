""" 
Algoritm:
The bubble_sort function takes an array arr as input.
It starts by setting the length of the array to n.
It uses two nested loops to iterate over the array:
The outer loop iterates n-1 times because after each iteration, the largest element is pushed to the end of the array.
The inner loop compares adjacent elements and swaps them if they are in the wrong order.
After n-1 iterations, the array will be sorted in ascending order.
The sorted array is then printed as output.
"""
def bubble_sort(arr):
    n = len(arr)
    print('The array after every iteration.')
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
# Example usage
numbers = [5, 3, 8, 2, 1]
bubble_sort(numbers)
print('final array:\n',numbers)