from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)
        for st in strs:
            k = tuple(sorted(st))
            # print(k)
            grams[k].append(st)

        return grams.values()

        

            
        