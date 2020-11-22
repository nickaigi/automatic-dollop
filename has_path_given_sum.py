class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def has_path_with_given_sum(node, s):
    if node is None:
        return (s == 0)
    else:
        ans = 0
        sub_sum = s - node.value

        if sub_sum == 0 and node.left == None and node.right == None:
            return True

        if node.left is not None:
            ans = ans or has_path_with_given_sum(node.left, sub_sum)
        if node.right is not None:
            ans = ans or has_path_with_given_sum(node.right, sub_sum)

        return ans
