# Sorting algo of two types :

# 1. Comparative - Bubble , selection, Insertion, Merge , Quick and Heap sort

# 2. Non-comparative  - Counting , Radix and Bucket sort
# Comparison Sort: A type of sort that determines the sorted order based on comparisons between the input elements.
# Non-comparison Sort: Sorting techniques that do not rely on element comparison and typically work with integer keys by grouping and counting elements.

# 1. Selection Sort

# The fundamental idea is to repeatedly find the smallest (or largest, depending on sorting order) element from the unsorted segment of the list and move it to the end of the sorted segment. This process is repeated for each of the elements until the entire array is sorted. The method divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list, and a sublist of the remaining unsorted items that occupy the rest of the list.


myArray = [64, 25, 12, 22, 11]


def selection_sort(nums: list):
    for indx in range(len(nums)):
        # Assume the current index has the minimum value
        min_index = indx

        # Find the index of the minimum element in the unsorted portion of the array
        for j in range(min_index + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        # Swap the minimum element with the first element of the unsorted portion
        nums[indx], nums[min_index] = nums[min_index], nums[indx]

    return nums


selection_sort(myArray)

# 2. Bubble Sort
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

myArray = [64, 25, 12, 22, 11]


def bubbleSort(arr):
    # Traverse through all array elements
    for i in range(len(arr) - 1):
        swapped = False
        # Last i elements are already in place, so inner loop runs for remaining elements
        for j in range(len(arr) - 1 - i):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break


def bubble_sort(my_array: list):
    nums = my_array.copy()

    for i in range(len(nums) - 1):
        swapped = False

        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break

    return nums


# 3. Insertion Sort
#  assumes that the first element is already sorted, then it goes through the remaining elements one by one, placing each in its proper position relative to those already sorted. The algorithm selects an element, compares it to the elements in the sorted section, and inserts it in the correct position by shifting all larger elements to the right. This process is repeated for each element until the entire array is organized
# https://www.youtube.com/watch?v=8mJ-OhcfpYg


def insertion_sort(my_array: list):
    nums = my_array.copy()

    for i in range(1, len(nums)):
        target_value = nums[i]  # value to be inserted

        j = i - 1

        while j >= 0 and nums[j] > target_value:
            # Shifting Element if it is greater than the target
            nums[j + 1] = nums[j]

            j -= 1

        # Insert the target value at the correct position
        # one index after the last element that was shifted.
        nums[j + 1] = target_value

    return nums


# Merge and Quick Sort pending
