class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals = sorted(intervals)
        i = 1
        prev = intervals[0]
        res = []
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev = [prev[0], max(prev[1], intervals[i][1])]
            else:
                res.append(prev)
                prev = intervals[i]
        res.append(prev)
        return res  
        
        
        