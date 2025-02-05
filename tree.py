from __future__ import annotations
from fraction import Fraction
from decimal_fraction import DecimalFraction
from mixed_fraction import MixedFraction

class Node:
    
    
    def __init__(self, val):
        if isinstance(val, (Fraction, DecimalFraction, MixedFraction)):
            if isinstance(val, DecimalFraction):
                self.value = DecimalFraction.to_fraction(val)
            elif isinstance(val, MixedFraction):
               self.value = MixedFraction.to_fraction(val)
            else:
                self.value = val
        else:
            raise TypeError("Argument must be Fraction or its successor")
        self.left = None
        self.right = None


class Tree:
    root:Node

    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        Node insertion method
        :param val: Node
        :return: None
        """
        if not isinstance(val, Fraction):
            val = Fraction(val)
        if self.root == None:
            self.root = Node(val)
        else:
            self.insertRec(self.root, val)

    def insertRec(self, node, val):
        """
        Node insertion recursive method
        :param node: Node
        :param val: Node
        :return: None
        """
        if val < node.value:
            if node.left is None:
                node.left = Node(val)
            else:
                self.insertRec(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.insertRec(node.right, val)

    def inorder_traversal(self):
        """
        Inorder traversing the tree method
        :return: None
        """
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        """
        Inorder traversing the tree recursive method
        :param node: Node
        :return: List
        """
        result = []
        if node:
            result = self._inorder_rec(node.left)
            #result.append(node.value.__str__())
            result.append(node.value)
            result += self._inorder_rec(node.right)
        return result

    def balance(self):
        """
        Tree balance method
        :return: None
        """
        sorted_values = self.inorder_traversal()
        self.root = self._sorted_array_to_bst(sorted_values)

    def _sorted_array_to_bst(self, sorted_values):
        """
        Tree sort method
        :param sorted_values: List
        :return: Node
        """
        if not sorted_values:
            return None
        mid = len(sorted_values) // 2
        node = Node(sorted_values[mid])
        node.left = self._sorted_array_to_bst(sorted_values[:mid])
        node.right = self._sorted_array_to_bst(sorted_values[mid + 1:])
        return node

    def print_tree(self):
        """
        Tree output method
        :return: None
        """
        self._print_tree_rec(self.root, 0)

    def _print_tree_rec(self, node, level):
        """
        Tree output recursive method
        :param node: None
        :param level: int
        :return: None
        """
        if node is not None:
            self._print_tree_rec(node.right, level + 1)
            print(' ' * 4 * level, node.value)
            self._print_tree_rec(node.left, level + 1)