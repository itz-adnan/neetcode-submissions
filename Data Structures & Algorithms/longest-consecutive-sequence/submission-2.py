class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        for i in nums:
            if i-1 in d:
                d[i] = d[i-1] + 1
            else:
                d[i] = 1

        if d:
            return max(d.values())
        return 0
        