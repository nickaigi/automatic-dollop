class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(inorder, preorder, in_start, in_end):
    """
    Recursive function to construct binary tree of size len(inorder) and
    len(preorder)
    Initial values of in_start and in_end should be 0 and (len - 1).
    The function doesn't do any error checking for cases where inorder and
    preorder do not form a tree
    """
    if in_start > in_end:
        return None


def restore_binary_tree(inorder, preorder):
    """
    inorder: traversal first visits the left subtree, then the root, then its
    right subtree
    preorder: traversal first visits the root, then its left subtree, then its
    right subtree

    Both inorder and preorder are integer arrays of the values found at the node
    """
    pass
