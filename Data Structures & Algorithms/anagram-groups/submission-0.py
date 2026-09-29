from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grams = []
        res = []

        for st in strs:
            st_count = Counter(st)
            try:
                i = grams.index(st_count)
                res[i].append(st)
            except:
                grams.append(st_count)
                res.append([st])

        return res

        

            
        