class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals = sorted(intervals)
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i] = [intervals[i-1][0],max(intervals[i-1][1], intervals[i][1])]
                intervals.pop(i-1)
            else:
                i+=1
        
        return intervals     
        
        
        