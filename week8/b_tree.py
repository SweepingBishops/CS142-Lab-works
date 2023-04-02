#!/usr/bin/env python
import colorama
colorama.init(autoreset=True)

class Node:
    '''Node object for a BTree'''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.subtree_size = 1


class BTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def from_list(arr: list) -> "BTree":
        '''Takes a list and return a balanced BTree object corresponding to the data.'''
        b_tree = BTree()
        del arr[0]
        arr.pop()
        mid_index = find_primary_operator(arr)
        b_tree.root = Node(arr[mid_index])
        def _recursion(parent, arr, side):
            if len(arr) == 0:
                return
            elif len(arr) == 1:
                if side == "left":
                    b_tree._add(parent, Node(int(arr[0])), "left")
                else:
                    b_tree._add(parent, Node(int(arr[0])), "right")
                return
            else:
                del arr[0]
                arr.pop()
            
            mid_index = find_primary_operator(arr)
            node =  Node(arr[mid_index])
            if side == "left":
                b_tree._add(parent, node, "left")
            else:
                b_tree._add(parent, node, "right")

            _recursion(node, arr[:mid_index],"left")
            _recursion(node, arr[mid_index+1:], "right")

        _recursion(b_tree.root, arr[:mid_index],"left")
        _recursion(b_tree.root, arr[mid_index+1:],"right")
        return b_tree

    def traverse(self, node="", arr=None):
        '''Return a list from the inorder traversal of the BTree.'''
        if arr is None:
            arr = list()
        if node == "":
            node = self.root
        if node is None:
            return
        self.traverse(node.left,arr)
        arr.append(node.data)
        self.traverse(node.right,arr)
        return arr

    def _add(self, parent, child, side):
        """
        Internal function to add a child to a node that doesn't have
        either a left or right child. 
        !! Do not add to a place that already has data. !!
        """
        child.parent = parent
        height = 1
        if side == "left":
            parent.left = child
        else:
            parent.right = child

        while parent:
            parent.subtree_size += 1
            if parent.height < height:
                parent.height = height
            
            height += 1
            parent = parent.parent

    def __getitem__(self, index):
        """Returns the ith node of the sequence."""
        node = self.root
        if index > self.root.subtree_size:
            return
        def _get_index(node, index):
            if node.left is None and index == 1:
                return node
            if node.left.subtree_size>=index:
                return _get_index(node.left, index)
            elif node.left.subtree_size+1==index:
                return node
            else:
                return _get_index(node.right, index-(node.left.subtree_size+1))
        return _get_index(node,index+1)

    def __setitem__(self, index, value):
        """Changes the value of the ith node."""
        self[index].data = value

    def insert(self, index, data):
        """Insert data at the index position."""
        prev = self[index]
        if prev.left is None:
            self._add(prev, Node(data), "left")
            return
        prev = prev.left
        while prev.right is not None:
            prev = prev.right
        self._add(prev, Node(data),"right")

    def delete(self, index):
        node = self[i]
        successor = self[i+1]

def find_primary_operator(expression):
    '''Takes an expression as a list as input, and returns
    the index of the primary operator.'''
    level = 0
    for index, char in enumerate(expression):
        if char == "(":
            level += 1
        elif char == ")":
            level -= 1
        elif char in "+-*/" and level == 0:
            return index

def solve(b_tree):
    def _solve(node):
        if node.left is None or node.right is None:
            return node.data
        left = _solve(node.left)
        right = _solve(node.right)
        
        if node.data == "+":
            return left+right
        elif node.data == "-":
            return left-right
        elif node.data == "*":
            return left*right
        elif node.data == "/":
            return left/right

    return _solve(b_tree.root)


if __name__ == "__main__":
    expression = "( ( 1 + 2 ) * ( ( 9 * 12 ) + 2 ) )".split()
    print(expression)
    b_tree = BTree.from_list(expression)
    print(b_tree.traverse())
    print(f"root: {b_tree.root.data}")
    print(f"root height: {b_tree.root.height}")
    print(f"tree size: {b_tree.root.subtree_size}")
    print(colorama.Fore.GREEN+f"Evaluated: {solve(b_tree)}")
    for i in range(b_tree.root.subtree_size):
        print(b_tree[i].data,end=",")
    print()

    print(b_tree[10].data)
    b_tree[b_tree.root.subtree_size-1]
    b_tree[1]="-"
    print(b_tree.traverse())
    print(colorama.Fore.GREEN+f"Evaluated after edit: {solve(b_tree)}")
    b_tree.insert(4,"test")
    print(b_tree.traverse())
