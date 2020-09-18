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




class Solution:
    def twoSum(self, nums, target):
        # brute force version - all tests passing except for one complaining about time limit exceeded
        indices = []
        print(nums)
        print(target)

       
        for i in range(len(nums)-1):
            counter = i+1
            while counter < len(nums):
                if nums[i] + nums[counter] == target:
                    indices.append(i)
                    indices.append(counter)
                    counter += 1
                    break
                else:
                    counter += 1
             

        print(indices)
        return indices
                

            




        

input_nums = [0,4,3,0]
input_target = 0
# Expected: [0,3]

solution = Solution()
solution.twoSum(input_nums, input_target)



