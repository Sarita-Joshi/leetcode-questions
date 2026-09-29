import collections as c
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = c.Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]

        for ele, counts in freq.items():
            buckets[counts].append(ele)
        
        res = []
        for i in range(len(buckets)-1,0,-1):
            for b in buckets[i]:
                res.append(b)
                if len(res)==k:
                    return res




