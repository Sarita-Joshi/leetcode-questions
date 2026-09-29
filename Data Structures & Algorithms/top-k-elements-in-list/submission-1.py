from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)

        return heapq.nlargest(k,hmap.keys(), key=hmap.get)