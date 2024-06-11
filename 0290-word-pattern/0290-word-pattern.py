class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        pairings = set(zip(pattern, s))
        # print(pairings)
        return len(pairings)==len(set(pattern))==len(set(s)) and len(pattern) == len(s)