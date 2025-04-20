# Description:
        # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        d = {}

        for i in range(0, len(nums)):
            num2 = target - nums[i]
            if num2 in d.keys():
                return [d[num2], i]
            else:
                d[nums[i]] = i 