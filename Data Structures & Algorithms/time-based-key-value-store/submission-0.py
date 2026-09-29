class TimeMap:

    def __init__(self):
        self.mapper = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapper[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapper or timestamp < self.mapper[key][0][1]:
            return ""
        data = self.mapper[key]
        l,r = 0,len(data)-1

        while l<=r:
            mid = (l+r)//2
            if data[mid][1]==timestamp:
                return data[mid][0]
            if data[mid][1] > timestamp:
                r = mid-1
            else:
                l = mid+1
        
        if data[r][1] < timestamp :
            return data[r][0]
        return ""

        
        
