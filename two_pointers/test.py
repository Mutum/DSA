# palindrome

def check_palindrome(test_string : str):

    test_string = test_string.lower()
    test_string = "".join(x for x in test_string if x != " ")

    left , right = 0 , len(test_string) -1

    while left < right:
        if test_string[left] != test_string[right]:
            return False
        
        left +=1
        right -=1
    
    return True

test_string = "mutum"
check_palindrome(test_string )

# Reversing an array: Given an array of integers, reverse it in place.

test_array = [1, 2, 3, 4,5]

def reverse_array(test_array : list):

    left , right = 0, len(test_array)-1

    while left < right:
        left_value , right_value = test_array[left], test_array[right]

        test_array[left] = right_value
        test_array[right] =left_value

        left +=1
        right -=1
    
    return test_array

reverse_array(test_array)

# Problem: 3Sum
# Given an integer array, nums, find and return all unique triplets [nums[i], nums[j], nums[k]], 
# such that i ≠j ,i≠k and j ≠k and nums[i] + nums[j] + nums[k] ==0

test_nums = [-3,-1,-1,0,1,2,3,3]

def three_sum(nums: list):
    nums.sort()  # sort entire list once
    result = []
    
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate fixed elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1  # two pointers
        while left < right:
            three_total = nums[i] + nums[left] + nums[right]
            
            if three_total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif three_total < 0:
                left += 1
            else:
                right -= 1
    
    return result


# Test
test_nums = [-3, -1, -1, 0, 1, 2, 3, 3]
print(three_sum(test_nums))

# sort colors
# Given an array, colors, which contains a combination of the following three elements:

# 0 (Representing red)
# 1 (Representing white)
# 2 (Representing blue)

# Sort the array in place so that the elements of the same color are adjacent,
#  and the final order is: red (0), then white (1), and then blue (2).

input_cols = [0,1,0]

def sort_colors(colors):
    # Initialize the start, current, and end pointers
    start, current, end = 0, 0, len(colors) - 1

    # Iterate through the list until the current pointer exceeds the end pointer
    while current <= end:
        if colors[current] == 0:
            # If the current element is 0 (red), swap it with the element at the start pointer
            # This ensures the red element is placed at the beginning of the array
            colors[start], colors[current] = colors[current], colors[start]
            # Move both the start and current pointers one position forward
            current += 1
            start += 1

        elif colors[current] == 1:
            # If the current element is 1 (white), just move the current pointer one position forward
            current += 1

        else:
            # If the current element is 2 (blue), swap it with the element at the end pointer
            # This pushes the blue element to the end of the array
            colors[current], colors[end] = colors[end], colors[current]
            # Move the end pointer one position backward
            end -= 1
    return colors

sort_colors(input_cols)
