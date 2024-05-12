class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        res = 0
        i=0
        while i < len(s):
            print(i, s[i])
            if s[i]=='I' and i+1<len(s):
                if s[i+1]=='V':
                    res += 4
                    i+=1
                elif s[i+1]=='X':
                    res+=9
                    i+=1
                else:
                    res+=1
            elif s[i]=='X' and i+1<len(s):
                if s[i+1]=='L':
                    res += 40
                    i+=1
                elif s[i+1]=='C':
                    res+=90
                    i+=1
                else:
                    res+=10
            elif s[i]=='C' and i+1<len(s):
                if s[i+1]=='D':
                    res += 400
                    i+=1
                elif s[i+1]=='M':
                    res+=900
                    i+=1
                else:
                    res+=100
            else:
                res += map[s[i]]
            i+=1

        return res