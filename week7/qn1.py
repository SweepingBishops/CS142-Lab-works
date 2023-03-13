#!/usr/bin/env python
"""
Question 1

Create a singly linked list with insert and delete operations at the beginning
and at the end where each node contains an alphabet and a number as data.
"""


class NotANodeError(Exception):
    """Raised when the value passed to the linked list is not of type node"""

    pass


class Node:
    '''Node object for the LinkedList'''
    def __init__(self, alpha, num):
        self.next = None
        self.alpha = alpha
        self.num = num
    
    def get_data(self):
        '''Returns the data of the node. In a tuple if there are multiple.'''
        return self.alpha, self.num


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        '''Appends given node to the end of the LinkedList'''
        if not isinstance(node, Node):
            raise NotANodeError("The value given was not of type 'Node'.")

        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node 

    def extend(self, node_iter):
        '''Extends the LinkedList using the given iterator of Nodes.'''
        prev_node = None
        for index, node in enumerate(node_iter):
            if not isinstance(node, Node):
                raise NotANodeError("The value given was not of type 'Node'.")

            if index == 0:
                self.append(node)
                prev_node = node
            else:
                prev_node.next = node
                prev_node = node

    def prepend(self, *nodes):
        '''Prepends given nodes to the start of the LinkedList'''
        for index, node in enumerate(nodes):
            if not isinstance(node, Node):
                raise NotANodeError("The value given was not of type 'Node'.")
            if index == 0:
                prev_node = None
            else:
                prev_node.next = node
                prev_node = node
        nodes[-1].next = self.head
        self.head = nodes[0]

    def pop(self):
        '''Removes the last node from the LinkedList and returns its value'''
        if self.head is None:
            raise IndexError("pop from empty LinkedList")

        if self.head.next is None:
            value = self.head.get_data()
            self.head = None
            return value

        current_node = self.head
        prev_node = None

        while current_node.next is not None:
            prev_node = current_node
            current_node = current_node.next

        prev_node.next = None
        return current_node.get_data()
            
    def remove_from_beginning(self):
        '''Removes the first node of the LinkedList and returns its value'''
        if self.head is None:
            raise IndexError("remove from emtpy LinkedList")

        if self.head.next is None:
            value = self.head.get_data()
            self.head = None
            return value

        value = self.head.get_data()
        self.head = self.head.next
        return value

    def get_data(self):
        '''Returns a list of the values of the nodes.'''
        if self.head is None:
            raise IndexError("empty LinkedList")

        data = list()
        current_node = self.head
        while current_node.next is not None:
            data.append(current_node.get_data())
            current_node = current_node.next
        data.append(current_node.get_data())
        return data

    def __str__(self):
        '''Prints the values of the nodes separated by a newline.'''
        values = [str(i) for i in self.get_data()]
        string = "\n".join(values)
        return string
