import random


class RandomizedSet:
    def __init__(self, array=None):
        self.array: set = set(array) if array else set()

    def insert(self, val: int) -> bool:
        if val in self.array:
            result = False
        else:
            result = True
        self.array.add(val)
        return result

    def remove(self, val: int) -> bool:
        if val in self.array:
            self.array.remove(val)
            result = True
        else:
            result = False
        return result

    def getRandom(self) -> int:
        if self.array:
            return random.choice(list(self.array))
        return None


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)  # true
param_2 = obj.remove(2)  # false
param_3 = obj.insert(2)  # Inserts 2 to the set, returns true. Set now contains [1,2]
param_4 = obj.getRandom()
param_5 = obj.remove(1)  # true
param_6 = obj.insert(2)  # false
param_7 = obj.getRandom()  # 2
