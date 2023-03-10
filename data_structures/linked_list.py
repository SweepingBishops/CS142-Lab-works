#!/usr/bin/env python
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self, *nodes):
        self.head = nodes[0]
        for index,node in enumerate(nodes):
            if index == 0:
                continue
            nodes[index-1].next = node

    def print(self):
        next_ = self.head
        while next_:
            print(next_.data)
            next_ = next_.next

    def add(self, node, index):
        if index == 0:
            node.next = self.head
            self.head = node
            return

        counter = 0
        pointer = self.head
        prev_pointer = None
        while counter < index:
            if x:= pointer.next:
                prev_pointer = pointer
                pointer = x
                counter += 1
            else:
                prev_pointer = pointer
                pointer = None
                break
        node.next = pointer
        prev_pointer.next = node

if __name__ == "__main__":
    n1 = node(1)
    n2 = node(2)
    n3 = node(3)
    l = linked_list(n1,n2,n3)
    l.print()
    print("*"*5)
    l.add(node(400), 0)
    l.print()
