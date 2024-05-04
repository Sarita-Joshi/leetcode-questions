
class Solution:
    ## Check predecessor function
    def verify(self, w1, w2):
        # Length should have a difference of 1 to checl for predecessor
        if len(w1) + 1 != len(w2):
            return False
        
        # Check if the strings match character by character
        # we can exclude 1 different of a character
        i, j = 0, 0
        excluded = False
        while i < len(w1) and j < len(w2):
            if w1[i] == w2[j]:
                i += 1
                j += 1
            else:
                if excluded:
                    return False
                j += 1
                excluded = True
        return True

    def longest_word_chain(self, words) -> int:
        # Sort the words by their length
        words.sort(key=len)
        
        # Dictionary to keep track of the maximum length of chain ending with each word
        counts = {word: 1 for word in words}
        
        # Calculate the longest chain possible
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.verify(words[i], words[j]):
                    # max of words[j] and words[i] plus 1
                    counts[words[j]] = max(counts[words[j]], counts[words[i]] + 1)
        
        # The longest chain will be the maximum value in counts
        return max(counts.values())


# Example usage
words = ["a", "b", "ba", "bca", "bda", "bdca"]

s = Solution()
longest_chain_length = s.longest_word_chain(words)
print("Longest chain length:", longest_chain_length)