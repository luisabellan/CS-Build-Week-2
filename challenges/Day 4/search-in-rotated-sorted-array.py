# You are given an integer array nums sorted in ascending order, and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# If target is found in the array return its index, otherwise, return -1.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:

# Input: nums = [1], target = 0
# Output: -1

 

# Constraints:

#     1 <= nums.length <= 5000
#     -10^4 <= nums[i] <= 10^4
#     All values of nums are unique.
#     nums is guranteed to be rotated at some pivot.
#     -10^4 <= target <= 10^4

def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                print(mid)
                return mid

            if nums[left] <= nums[mid]:  # LHS is sorted
                if target >= nums[left] and target < nums[mid]:  # target is on LHS
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # RHS is sorted
                if target <= nums[right] and target > nums[mid]:  # target is on RHS
                    left = mid + 1
                else:
                    right = mid - 1
        print(-1)
        return -1


# nums = [1]
# target = 0
# # expected: -1

# nums = [4,5,6,7,0,1,2]
# target = 3
# # expected: -1

nums = [4,5,6,7,0,1,2]
target = 0
# expected: 4

search(nums,target)