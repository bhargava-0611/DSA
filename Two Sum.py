class Solution:
    def twoSum(self, nums, target):
        nums_null = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_null: 
                return [nums_null[target - nums[i]], i]
            nums_null[nums[i]] = i
        
