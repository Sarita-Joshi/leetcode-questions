class Solution:
    def hammingWeight(self, n: int) -> int:
      n = format(n, 'b')
      return n.count('1')