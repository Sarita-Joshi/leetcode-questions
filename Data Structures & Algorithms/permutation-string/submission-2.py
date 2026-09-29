class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = defaultdict(int)
        freq_s2 = defaultdict(int)
        l = r = 0
        size = len(s1)

        for s in s1:
            freq_s1[s]+=1

        def compare(d):
            for k,v in freq_s1.items():
                if d.get(k) != v:
                    return False
            return True

        for r in range(len(s2)):
            print(s2[l:r], freq_s2)
            freq_s2[s2[r]] += 1
            if r-l >= size:
                freq_s2[s2[l]]-=1
                l+=1
            if compare(freq_s2):
                return True
        return False
                
            
            

