class Solution:
    def majorityElement(self, nums: List[int]) -> int: # type: ignore
        d = {}

        for item in nums:
            if item in d.keys():
                d[item] += 1
            else: 
                d[item] = 1

        for item in d.keys():
            if d[item] > (len(nums)) // 2:
                return item
            
        