class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # mapper = {}

        # for i,n in enumerate(numbers):
        #     comp = target -n
        #     if comp!=n and comp in mapper:
        #         return [mapper[comp]+1,i+1]
        #     mapper[n] = i

        l, r = 0, len(numbers)-1

        while l < r:
            total = numbers[l]+numbers[r]
            if total > target:
                r-=1
            elif total < target:
                l+=1
            else:
                return [l+1,r+1]