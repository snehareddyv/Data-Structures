class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]: # type: ignore
        highest = max(candies)
        for i in range(0, len(candies)): 
            if candies[i] + extraCandies >= highest:
                candies[i] = True
            else:
                candies[i] = False
        return candies