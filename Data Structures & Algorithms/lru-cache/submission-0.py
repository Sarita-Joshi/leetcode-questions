class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.q = []
        self.d = {}

    def get(self, key: int) -> int:
        if key in self.d:
            self.q.remove(key)
            self.q.append(key)
            print('gt',self.q, self.d)
            return self.d[key]
        print('gt',self.q, self.d)
        return -1
        
    def put(self, key: int, value: int) -> None:
        print('pt',self.q, self.d)
        if len(self.q) == self.cap and key not in self.d:
            k = self.q.pop(0)
            del self.d[k]
        if key in self.d:
            self.q.remove(key)
        self.q.append(key)
        self.d[key] = value


        
