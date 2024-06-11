class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs)==1:
            return [strs]
        
        res = defaultdict(list)
        
        for s in strs:
            res[tuple(sorted(s))].append(s)
        
        return list(res.values())
            
            