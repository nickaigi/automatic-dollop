class Tree(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def is_tree_symmetric(root):


    def is_mirror(left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            if left.value == right.value:
                return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
            else:
                return False

    if root is None:
        return True
    else:
        return is_mirror(root.left, root.right)
