class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        prev = 0
        total = 0

        for i in range(0, len(s)):
            curr = d[s[i]]
            if curr > prev:
                total = total + curr - 2 * prev
            else:
                total += curr
            prev = curr

        return total       