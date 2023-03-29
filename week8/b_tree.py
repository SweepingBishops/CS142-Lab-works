#!/usr/bin/env python
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
        mid_index = len(arr)//2
        b_tree.root = Node(arr[mid_index])
        def _recursion(parent, arr, side):
            if len(arr) == 0:
                return
            elif len(arr) == 1:
                if side == "left":
                    b_tree._add(parent, Node(arr[0]), "left")
                else:
                    b_tree._add(parent, Node(arr[0]), "right")
                return
            
            mid_index = len(arr)//2
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


if __name__ == "__main__":
    b_tree = BTree.from_list([1,1,2,3,4,5,6,7])
    print(b_tree.traverse())
    print(f"root: {b_tree.root.data}")
    print(f"root height: {b_tree.root.height}")
    print(f"tree size: {b_tree.root.subtree_size}")
    print(f"test height: {b_tree.root.right.height}")
    print(f"test size: {b_tree.root.right.subtree_size}")
    b_tree._add(b_tree.root.right.right, Node(100), "right")
    print(b_tree.traverse())
    print(f"test size: {b_tree.root.right.subtree_size}")
    print(f"test height: {b_tree.root.right.height}")
    print(f"root height: {b_tree.root.height}")
    print(f"tree size: {b_tree.root.subtree_size}")
