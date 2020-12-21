# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true

# Example 2:

# Input: [1,2,3,4]
# Output: false

# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true




class Solution:
    def containsDuplicate(self, nums):
        self.nums = nums
        if len(self.nums) == len(set(self.nums)):
            print(False)
            return False
        else:
            print(True)
            return True

nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

Solution().containsDuplicate(nums1)
Solution().containsDuplicate(nums2)
Solution().containsDuplicate(nums3)

        

