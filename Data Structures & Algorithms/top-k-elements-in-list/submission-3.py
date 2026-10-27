class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        return [i[0] for i in sorted(collections.Counter(nums).items(), key=lambda item: item[1], reverse=True)[:k]]