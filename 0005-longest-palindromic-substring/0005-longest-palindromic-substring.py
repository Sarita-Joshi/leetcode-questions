class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n==1: return s
        if n==2: return s[0] if s[0]!= s[1] else s 

        def expandCenter(left, right):
            while left >= 0 and right <= n-1 and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]

        maxlen = s[0]
        for i in range(n-1):
            odd = expandCenter(i,i)
            even = expandCenter(i,i+1)
            if len(odd) > len(maxlen):
                maxlen = odd
            if len(even) > len(maxlen):
                maxlen = even

        return maxlen