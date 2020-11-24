class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def kth_smallest_in_bst(node, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            break
        root = root.right
    return root.value
