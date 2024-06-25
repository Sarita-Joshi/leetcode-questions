class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.insert(0, beginWord)
            
        n = len(wordList)
        
        def diff(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    count += 1
            return count == 1
        
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if diff(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while q:
            curr, steps = q.popleft()
            
            for w in adj[curr]:
                if w == endWord:
                    return steps + 1
                if w not in visited:
                    visited.add(w)
                    q.append((w, steps+1))
        
        return 0
        