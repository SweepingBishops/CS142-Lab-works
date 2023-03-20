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
    """Node object for the LinkedList"""

    def __init__(self, alpha, num):
        self.next = None
        self.alpha = alpha
        self.num = num

    def get_data(self):
        """Returns the data of the node. In a tuple if there are multiple."""
        return self.alpha, self.num


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def append(self, node):
        """Appends given node to the end of the LinkedList"""
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
        """Extends the LinkedList using the given iterator of Nodes."""
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
        """Prepends given nodes to the start of the LinkedList"""
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
        """Removes the last node from the LinkedList and returns its value"""
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
        """Removes the first node of the LinkedList and returns its value"""
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
        """Returns a list of the values of the nodes."""
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
        """Prints the values of the nodes separated by a newline."""
        values = [str(i) for i in self.get_data()]
        string = "\n".join(values)
        return string

    def is_palindrome(self):
        """Checks if the alphabets of the nodes make a palindrome."""
        slow_node, fast_node = self.head, self.head
        prev = None
        flag = False
        while True:
            if fast_node is None:
                break
            elif fast_node.next is None:
                flag = True
                break
            fast_node = fast_node.next.next
            slow_node.next, slow_node, prev = prev, slow_node.next, slow_node

        left_node = prev
        prev = slow_node
        if flag:
            right_node = slow_node.next
        else:
            right_node = slow_node
        palindrome = True
        while left_node:
            if left_node.alpha != right_node.alpha:
                palindrome = False
            right_node = right_node.next
            left_node.next, left_node, prev = prev, left_node.next, left_node
        return palindrome

    def insertion_sort(self):
        """Sorts the LinkedList using the Insertion Sort algorithm"""
        if self.is_empty():
            return None
        unsorted_head = self.head.next
        last_sorted = self.head
        while unsorted_head:
            if last_sorted.num <= unsorted_head.num:
                unsorted_head = unsorted_head.next
                last_sorted = last_sorted.next
                continue
            last_sorted.next = unsorted_head.next
            if self.head.num > unsorted_head.num:
                unsorted_head.next, unsorted_head, self.head = (
                    self.head,
                    unsorted_head.next,
                    unsorted_head,
                )
                continue
            node = self.head
            while unsorted_head.num > node.next.num:
                node = node.next
            node.next, unsorted_head.next, unsorted_head = (
                unsorted_head,
                node.next,
                unsorted_head.next,
            )

    def merge_sort(self):
        """Sorts the LinkedList using the Merge Sort algorithm"""
        if self.is_empty():
            return
        self.head = self._merge_sort("FIRST_CALL")

    def _merge_sort(self, head):
        if head == "FIRST_CALL":
            head = self.head
        if head.next == None:
            return head
        fast_node, slow_node = head.next, head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        right_node = slow_node.next
        slow_node.next = None
        head = self._merge_sort(head)
        right_node = self._merge_sort(right_node)
        return self._merge(head, right_node)

    def _merge(self, left_node, right_node):
        dummy_node = Node(None, None)
        node = dummy_node
        while left_node and right_node:
            if left_node.num < right_node.num:
                node.next = left_node
                node = left_node
                left_node = left_node.next
            else:
                node.next = right_node
                node = right_node
                right_node = right_node.next

        if left_node:
            node.next = left_node
        elif right_node:
            node.next = right_node
        return dummy_node.next


if __name__ == "__main__":
    l_list = LinkedList()
    alphas = list("abcdcba")
    nums = [int(i) for i in "4320561"]
    nodes = [Node(a, n) for a, n in list(zip(alphas, nums))]
    l_list.extend(nodes)
    print(l_list)
    print(f"Is a palindrome: {l_list.is_palindrome()}")
    print("*" * 10)
    l_list.merge_sort()
    print(l_list)
