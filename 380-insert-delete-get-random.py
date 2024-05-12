import random

class RandomizedSet:

    def __init__(self):
        self.table = dict()
        self.vallist = []

    def insert(self, val: int) -> bool:
        if val in self.table:
            return False
        self.table[val]= len(self.vallist)
        self.vallist.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.table:
            return False
        i = self.table[val]
        self.vallist[i] = self.vallist[-1]
        self.table[self.vallist[-1]] = i

        del self.table[val]
        self.vallist.pop()
        return True

    def getRandom(self) -> int:
        n = random.randint(0,len(self.vallist)-1)
        return self.vallist[n]

