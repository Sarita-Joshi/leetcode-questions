class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = r = 0
        freq = defaultdict(int)

        def get_max():
            return max(freq.values())
            

        for r in range(len(s)):
            freq[s[r]] += 1
            # print(freq, (r-l+1), get_max())
            while r - l + 1 - get_max() > k:
                # print((r-l), get_max())
                freq[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)

        return max(res, r-l+1)
                