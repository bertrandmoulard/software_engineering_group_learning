class HashMap:
    def __init__(self, size=200):
        self.size = size
        self.keys, self.values= [[] for i in range(size)], [[] for i in range(size)]

    def put(self, key, value):
        i = self._hash(key)
        if key in self.keys[i]:
            self.values[i][self.keys[i].index(key)] = value
        else:
            self.keys[i].append(key)
            self.values[i].append(value)

    def get(self, key):
        i = self._hash(key)
        if key in self.keys[i]:
            return self.values[i][self.keys[i].index(key)]
        else:
            return None

    def remove(self, key):
        i = self._hash(key)
        if key in self.keys[i]:
            idx = self.keys[i].index(key)
            self.keys[i].pop(idx)
            self.values[i].pop(idx)

    def _hash(self, key):
        return hash(key) % self.size

    def __str__(self):
        return self.keys.__str__() + "\n" + self.values.__str__()

#standard case
map = HashMap(10)
map.put("one", 1)
map.put("two", 2)
assert(map.get("one") == 1)
assert(map.get("two") == 2)
assert(map.get("three") == None)

#force collisions
map = HashMap(1)
map.put("one", 1)
map.put("two", 2)
assert(map.get("one") == 1)
assert(map.get("two") == 2)
assert(map.get("three") == None)

#default size
map = HashMap()
map.put("one", 1)
map.put("two", 2)
assert(map.get("one") == 1)
assert(map.get("two") == 2)
assert(map.get("three") == None)

#remove
map = HashMap()
map.put("one", 1)
map.put("two", 2)
assert(map.get("one") == 1)
assert(map.get("two") == 2)
map.remove("two")
assert(map.get("two") == None)
