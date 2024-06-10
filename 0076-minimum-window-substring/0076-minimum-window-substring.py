class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t or len(s) < len(t):
            return ""
        
        t_count = collections.Counter(t)

        count = len(t)
        start=0
        end=0
        minlen=len(s)+1
        start_index=0
        
        while end < len(s):
            if s[end] in t_count:
                if t_count[s[end]] > 0:
                    count -= 1
                t_count[s[end]] -= 1
            end += 1
            
            while count == 0:
                if end - start < minlen:
                    start_index=start
                    minlen = end-start
                
                if s[start] in t_count:
                    if t_count[s[start]] == 0:
                        count += 1
                    t_count[s[start]] += 1
                    
                start += 1
        if minlen ==len(s)+1:
            return ""
        return s[start_index: start_index+minlen]
                
                    
                    
            
            
            ## get next closest index if double count found
            
            
                    
                    
                
                
            
            
        
        
        
        return ""
        
        
        
        
        
        
        
        
        
#         if not s or not t or len(s) < len(t):
#             return ""

#         map = [0] * 128
#         count = len(t)
#         start = 0
#         end = 0
#         min_len = float('inf')
#         start_index = 0
#         # UPVOTE !
#         for char in t:
#             map[ord(char)] += 1

#         while end < len(s):
#             if map[ord(s[end])] > 0:
#                 count -= 1
#             map[ord(s[end])] -= 1
#             end += 1

#             while count == 0:
#                 if end - start < min_len:
#                     start_index = start
#                     min_len = end - start

#                 if map[ord(s[start])] == 0:
#                     count += 1
#                 map[ord(s[start])] += 1
#                 start += 1

#         return "" if min_len == float('inf') else s[start_index:start_index + min_len]