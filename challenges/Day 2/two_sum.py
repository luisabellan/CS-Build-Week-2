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
        
        indices = []
        print('nums',nums) # [0, 4, 3, 0]

        print('target',target) # 0

        # print('here',table[target])
        table = create_table()
        print(table)
        x = table[target][0]
        y = table[target][1]
        
        index = nums.index(x)
        
        print([nums.index(x),nums.index(y,index+1)])
      
       

            

input_nums = [0,4,3,0]
input_target = 0
# Expected: [0,3]


solution = Solution()
solution.twoSum(input_nums, input_target)



