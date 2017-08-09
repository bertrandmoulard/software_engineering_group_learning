from hashmap_bucket import HashmapBucket

class HashMap:
    def __init__(self, size=200):
        self.size = size
        self.buckets = [HashmapBucket() for i in range(size)]

    def put(self, key, value):
        self.buckets[self._hash(key)].put(key, value)

    def get(self, key):
        return self.buckets[self._hash(key)].get(key)

    def remove(self, key):
        self.buckets[self._hash(key)].remove(key)

    def _hash(self, key):
        return hash(key) % self.size

if __name__ == "__main__":
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
