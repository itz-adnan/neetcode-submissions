class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for i in range(len(nums)):
            other = target - nums[i]
            if other in seen:
                return [nums.index(other), i]
            seen.add(nums[i])