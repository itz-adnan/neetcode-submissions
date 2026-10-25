class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        
        res = []
        lst = list(freq.items())
        lst.sort(key = lambda x:-x[1])
        for i in range(k):
            res.append(lst[i][0])

        return res