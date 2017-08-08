class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        s = "["
        if self.prev is not None:
            s += self.prev.value + " <> "
        else:
            s += "none <> "
        s += self.value
        if self.next is not None:
            s += " <> " + self.next.value
        else:
            s += " <> none"
        s += "]"
        return s

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_at_beginning(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.head.prev = n
            n.next = self.head
            self.head = n
        return self


    def add_at_end(self, value):
        n = Node(value)
        if self.tail is None:
            self.head = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        return self

    def remove_first_occurence(self, value):
        n = self.head
        while n is not None:
            if n.value == value:
                if n is not self.tail and n is not self.head:
                    n.prev.next = n.next
                    n.next.prev = n.prev
                else:
                    if n == self.head:
                        self.head = n.next
                        if self.head is not None:
                            self.head.prev = None
                    if n == self.tail:
                        self.tail = n.prev
                        if self.tail is not None:
                            self.tail.next = None
                break
            n = n.next
        return self

    def __str__(self):
        n, s = self.head, ""
        while n is not None:
            s += str(n)
            n = n.next
        return s


l = DLinkedList()
res = l.add_at_beginning("one")
assert(res == l)
assert(l.head.value == "one")
assert(l.tail.value == "one")
assert(l.head.next == None)
assert(l.tail.prev == None)
l.add_at_beginning("two")
assert(l.head.value == "two")
assert(l.head.next.value == "one")
assert(l.tail.value == "one")
assert(l.tail.prev.value == "two")
l.add_at_beginning("three")
assert(l.head.value == "three")
assert(l.head.next.value == "two")
assert(l.tail.value == "one")
assert(l.tail.prev.value == "two")

l = DLinkedList()
res = l.add_at_end("zero")
assert(res == l)
assert(l.head.value == "zero")
assert(l.tail.value == "zero")
l.add_at_end("one")
assert(l.head.value == "zero")
assert(l.head.next.value == "one")
assert(l.tail.value == "one")
assert(l.tail.prev.value == "zero")
l.add_at_end("two")
assert(l.head.value == "zero")
assert(l.head.next.value == "one")
assert(l.tail.value == "two")
assert(l.tail.prev.value == "one")

l = DLinkedList()
l.add_at_end("zero").add_at_end("one").add_at_end("two")
res = l.remove_first_occurence("one")
assert(res == l)
assert(l.head.value == "zero")
assert(l.tail.value == "two")
assert(l.head.next.value == "two")
l = DLinkedList()
l.add_at_end("zero").add_at_end("one").add_at_end("two")
l.remove_first_occurence("zero")
assert(l.head.value == "one")
assert(l.tail.value == "two")
assert(l.head.next.value == "two")
l = DLinkedList()
l.add_at_end("zero").add_at_end("one").add_at_end("two")
l.remove_first_occurence("two")
assert(l.head.value == "zero")
assert(l.tail.value == "one")
assert(l.head.next.value == "one")
l = DLinkedList()
l.add_at_end("zero")
l.remove_first_occurence("zero")
assert(l.head == None)
assert(l.tail == None)
