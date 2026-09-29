class Solution:


    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(st)}|{st}" for st in strs])
        

    def decode(self, s: str) -> List[str]:
        if s=="":
            return []
        if s=="0|":
            return [""]
            
        res = []
        while s:
            temp = s.split("|", 1)
            c, s = temp[0], temp[1]
            res.append(s[:int(c)])
            s = s[int(c):]
        return res


