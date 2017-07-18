class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_at_end(self, value):
        node = Node(value)
        if (not self.head):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return self

    def add_at_beginning(self, value):
        node = Node(value)
        if (not self.head):
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        return self

    def has_cycle(self):
        node_one = self.head
        node_two = self.head

        while node_two is not None:
            node_two = node_two.next
            node_two = node_two.next
            node_one = node_one.next
            if node_two is node_one:
                return true

        return false

    def make_cycle(self):
        self = LinkedList()
        self.head = Node("a")
        self.head.next = Node("b")


    def __str__(self):
        string = ''
        current_node = self.head
        while current_node is not None:
            string += current_node.value
            current_node = current_node.next
            if current_node is not None:
                string += ' -> '
        return string

    def _swap_head_and_tail(self):
        self.tail.next = self.head
        self.head.next = None
        self.head, self.tail = self.tail, self.head

    def reverse_in_place(self):
        if self.size < 2:
            pass
        elif self.size == 2:
            self._swap_head_and_tail()
        else:
            current = self.head
            nxt = current.next
            two_nxt = nxt.next
            current.next = None
            self.tail = current
            while two_nxt is not None:
                nxt.next = current
                current = nxt
                nxt = two_nxt
                two_nxt = two_nxt.next
            nxt.next = current
            self.head = nxt
        return self


# add_at_end
a_list = LinkedList()
a_list.add_at_end("Ivan").add_at_end("Mike").add_at_end("Bertrand").add_at_end("Nicole").add_at_end("Mackenzie").add_at_end("Bernard")
assert(a_list.head.value == "Ivan")
assert(a_list.tail.value == "Bernard")

# reverse
a_list.reverse_in_place()
assert(a_list.head.value == "Bernard")
assert(a_list.head.next.value == "Mackenzie")
assert(a_list.tail.value == "Ivan")

a_list = LinkedList()
a_list.add_at_beginning("Michelle")
assert(a_list.size == 1)
a_list.reverse_in_place()
assert(a_list.head.value == "Michelle")


a_list = LinkedList()
a_list.add_at_beginning("Michelle").add_at_end("Bernard")
assert(a_list.size == 2)
a_list.reverse_in_place()
assert(a_list.head.value == "Bernard")
assert(a_list.tail.value == "Michelle")
