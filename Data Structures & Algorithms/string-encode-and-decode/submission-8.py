class Solution:


    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(st)}|{st}" for st in strs])
        

    def decode(self, s: str) -> List[str]:
        if s=="":
            return []
        if s=="0|":
            return [""]
            
        res = []
        i=0
        while i<len(s):
            j=i
            while s[j]!="|":
                j+=1

            c = int(s[i:j])
            res.append(s[j+1:j+c+1])
            i=j=j+c+1
            
        return res


