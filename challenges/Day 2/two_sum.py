# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

 

# Constraints:

#     2 <= nums.length <= 105
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.



# hashmap



import random
import math




def create_table():
    # keys will be arrays holding x and y, where x
    table = {}

    for x in range(0, 10): # -109,110
        for y in range(0,10):
            
            table[x + y] =  (x, y)
    print(table)
    return table.get((x,y))
    # return table




class Solution:
    def twoSum(self, nums, target):
        
        sums = []
        hashTable = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashTable:
                # print("Pair", target,"is: (", nums[i],",",complement,")")
                print(f'solution: {[i, nums.index(complement)]}')
                return [i, nums.index(complement)]
            hashTable[nums[i]] = nums[i]

            

input_nums = [3,2,4]
input_target = 6
# Expected: [0,1]


solution = Solution()
solution.twoSum(input_nums, input_target)



