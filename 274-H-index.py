class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==1:
            if citations[0]>=1: return 1
            else: return 0
        citations.sort()
        n = len(citations)
        count = 0
        for i in range(n-1, -1, -1):
            if citations[i] >= n-i:
                count+=1
            else:
                break
        return count