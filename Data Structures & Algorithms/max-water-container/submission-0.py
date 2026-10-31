class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        curr_max = 0
        
        while left != right:
            res = min(heights[left], heights[right])*(right-left)
            if res > curr_max:
                curr_max = res
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return curr_max