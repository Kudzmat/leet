"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


# this solution has O(n) because we iterate through the list once
def two_nums(my_list, target):
    my_map = {}  # this has map will hold the number(value) and index of each item in the list num : index

    for index, num in enumerate(my_list):
        diff = target - num  # find the difference between the target and the num at the specific index

        # we will check to see if the difference is already in the hash map
        if diff in my_map:
            return [my_map[diff],
                    index]  # if it is there, we will return the index (using the difference as a key) & the current index
        else:
            my_map[num] = index  # if it's not there we add the num & value to the map


# hash table
employee_details = {'Employee': {'Dave': {'ID': '001', 'salary': '2000', 'role': 'manager'},
                                 'Zelda': {'ID': '002', 'salary': '1500', 'role': 'jnr manager'}}}

# accessing values
employee_details.keys()
employee_details.get('Employee')
employee_details.values()

# updating
employee_details['Employee']['Zelda']['ID'] = '004'

nums = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 3]
target = 6

print(two_nums(nums2, target2))
