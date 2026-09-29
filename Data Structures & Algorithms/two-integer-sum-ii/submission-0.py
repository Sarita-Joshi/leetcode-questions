class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapper = {}

        for i,n in enumerate(numbers):
            comp = target -n
            if comp!=n and comp in mapper:
                return [mapper[comp]+1,i+1]
            mapper[n] = i