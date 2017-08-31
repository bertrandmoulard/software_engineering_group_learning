class Node:
    def __init__(self, key=None, value=None, next_el=None):
        self.key = key
        self.value = value
        self.next_el = next_el

class HashmapBucket:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, key, value):
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next_el
        self._add_at_end(key, value)

    def get(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next_el
        return None

    def remove(self, key):
        current = self.head
        prev = None
        while current is not None:
            if current.key == key:
                if current is self.head:
                    if current.next_el is None:
                        self.head = None
                        self.tail = None
                    #  else:
                        self.head = current.next_el
                elif current is self.tail:
                    self.tail = prev
                    self.tail.next_el = None
                else:
                    prev.next_el = current.next_el
                break
            prev = current
            current = current.next_el


    def _add_at_end(self, key, value):
        node = Node(key, value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_el = node
            self.tail = node


if __name__ == "__main__":
    l = HashmapBucket()
    l.put("hello", "bonjour")
    assert(l.get("hello") == "bonjour")
    assert(l.get("bye") == None)

    l.remove("hello")
    assert(l.get("hello") == None)

    l.put("hello", "bonjour")
    l.put("bye", "au revoir")
    assert(l.get("hello") == "bonjour")
    assert(l.get("bye") == "au revoir")
    l.put("later", "a plus")
    assert(l.get("later") == "a plus")
    l.remove("later")
    l.remove("bonjour")
    assert(l.get("bye") == "au revoir")
    l.remove("bye")
    assert(l.get("bye") == None)

