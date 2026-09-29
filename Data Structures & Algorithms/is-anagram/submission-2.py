from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return True

        return Counter(s)==Counter(t)
