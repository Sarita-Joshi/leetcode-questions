class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, line, chars = [],[],0
        
        for w in words:
            if chars + len(w) + len(line) > maxWidth:
                ## append spaces at the end
                l = len(line)-1 or 1
                for i in range(maxWidth - chars):
                    line[i % l] += " " 
                res.append(''.join(line))
                line = []
                chars = 0
            line.append(w)
            chars += len(w)
            
        if line:
            line = ' '.join(line) + " "* (maxWidth - chars - len(line) + 1)
            res.append(line)
        
        return res
                
            
            
            
        