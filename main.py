"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


# use set to check if value already exists
def is_distinct(my_list):

    # Because sets cannot have multiple occurrences of the same element, it makes sets highly useful to efficiently
    # remove duplicate values from a list
    my_set = set()

    for num in my_list:
        if num in my_set:
            return True
        else:
            my_set.add(num)

    return False


nums = [1, 2, 3, 2]
nums2 = [4, 2, 3, 1]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(nums3.index(3))

print(is_distinct(nums3))
