class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for s in strs:
            hmap[str(sorted(s))].append(s)

        return list(hmap.values())