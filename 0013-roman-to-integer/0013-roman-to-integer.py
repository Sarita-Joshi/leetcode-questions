class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D": 500,
            "M":1000
        }
        
        result = 0
        n = len(s)
        for i in range(n):
            if i < n-1 and mapper[s[i]] < mapper[s[i+1]]:
                result -= mapper[s[i]]
            else:
                result += mapper[s[i]]
        return result
        