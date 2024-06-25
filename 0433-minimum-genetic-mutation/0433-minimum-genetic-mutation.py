class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if not bank: 
            return -1
        
        if startGene not in bank:
            bank.insert(0, startGene)
        
        n = len(bank)
        
        def diff(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    count+=1
            return count == 1
        
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if diff(bank[i], bank[j]):
                    adj[bank[i]].append(bank[j])
                    adj[bank[j]].append(bank[i])
        
        q = deque([(startGene, 0)])
        visited = []
        while q:
            curr, count = q.popleft()
            for a in adj[curr]:
                if a == endGene:
                    return count+1
                if a not in visited:
                    visited.append(a)
                    q.append((a,count+1))
        return -1
                
            
        
                    
                    
        