class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: # type: ignore
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid 
            elif nums[mid] < target: 
                left = mid + 1

        return left

        