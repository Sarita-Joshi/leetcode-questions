class Solution:
    
## Use Sieve of Eratosthenes
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        
        isprime = [True] * n
        isprime[0]=isprime[1]=False

        for i in range(2, int(n**0.5)+1):
            if isprime[i]==True:
                for j in range(i*i, n, i):
                    isprime[j]=False
        
        count=0
        for i in range(2,n):
            if isprime[i]:
                count+=1
        return count