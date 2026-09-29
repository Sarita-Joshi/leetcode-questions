class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        post = [nums[-1]]
        l = len(nums)
        for i in range(1,l):
            pre.append(pre[i-1]*nums[i])
        
        for i in range(l-2, -1, -1):
            post.insert(0, post[0]*nums[i])
        
        res = []
        for i in range(l):
            if i==0:
                res.append(post[i+1])
            elif i==l-1:
                res.append(pre[i-1])
            else:
                res.append(pre[i-1]*post[i+1])
        return res
    


            