class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: # type: ignore
        d = {}
        for item in nums: 
            if item in d.keys():
                d[item] += 1
                return True
            else:
                d[item] = 1

        return False
        