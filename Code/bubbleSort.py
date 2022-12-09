import numpy as np
import time


# Bubble sort algorithm
def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# User input size
arraySize = input("Please enter array size: ")

# Generate numbers of size n
numbers = np.arange(int(arraySize))
np.random.shuffle(numbers)
print("Generated list of size " + str(arraySize) + " is:" + str(numbers))

# start script with parallel processes
start_time = time.time()

# bubble_sort(numbers)
insertionSort(numbers)
print("\n\n Sorted Array: " + str(numbers))

# End of script
print("\n\n Execution Time --- %s seconds ---" % (time.time() - start_time))
