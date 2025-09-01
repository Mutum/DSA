# Linear Search

# Simplest search that iteratively search from the beginning of the object say array until it finds/match with the target. 
# At worst , it will search till the end that result in no matching or matching
# time complexity of O(n)

def linear_search(arr : list, target : float):

    # search for target and return the index position if match
    for idx in arr:
        if arr[idx]==target:
            return idx
    return -1

# Binary Search
# Binary search is an efficient algorithm to find the position of a target in a sorted array. It works by repeatedly dividing the search range in half:

# Steps:
# Start with two pointers: low (start) and high (end).
    # Find the middle index: mid = (low + high) // 2.
    # Compare the middle element with the target:
        # If equal, return the index.
        # If target < middle, search the left half (high = mid - 1).
        # If target > middle, search the right half (low = mid + 1).
    # Repeat until the target is found or the range is empty.

# Time Complexity: O(log(n))
# Space Complexity : O(1) iterative or O(log(n)) recursive

def binary_search(arr : list , target : float):

    low , high = 0 , len(arr)-1
    arr.sort()

    while low < high:

        #find mid index
        mid_indx = (low + high ) // 2

        if arr[mid_indx] == target: 
            return mid_indx
        elif target < arr[mid_indx]: # focus on left side
            high = mid_indx -1
        elif target > arr[mid_indx]: # focus on right side 
            low = mid_indx +1 
    return -1


# Exercise 
# Mininum in Rotated Array
# you are given a sorted array nums that has been rotated. The array
# contains unique integers. Find and return the minimum value in the array

# eg. nums = [8,9,10,1,2,3,4]
# output = 1
# explanation : the original array was
# [1,2,3,4,8,9,10] rotated 3 times.

def find_min(arr : list):
    # linear search

    min_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

def find_min_binary_search(arr : list):
    # by binary search
    if len(arr) < 1:
        return arr[0]

    left , right = 0 , len(arr)-1

    while left < right:

        mid_indx = (left + right)//2
        if arr[mid_indx] > arr[right]:
            # if it is, then the minimum must be in the right half
            left = mid_indx+1
        else :
            # if it is not, then the minimum must be on the left side including mid
            right = mid_indx
    return arr[left]

# You are given a sorted array nums rotated at an unknown pivot. Find the index of a target value
# or return -1 if the target is not in the array 
# eg nums = [6,7,8,1,2,3,4] target = 3
# output 5

def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is the target
        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[low] <= nums[mid]:  # Left half is sorted
            if nums[low] <= target < nums[mid]:  # Target in left half
                high = mid - 1
            else:  # Target in right half
                low = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[high]:  # Target in right half
                low = mid + 1
            else:  # Target in left half
                high = mid - 1

    # Target not found
    return -1

# Example usage
nums = [6, 7, 8, 1, 2, 3, 4]
target = 3
print(search(nums, target))  # Output: 5
