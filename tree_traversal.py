class Tree(object):
    def __init__(self, x):
        self.value = x
        self.right = None
        self.left = None



def traverse(node):
    value = 0
    if node:
        pass


def print_tree(node):
    if node:
        print(node.value)
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)



if __name__ == '__main__':
    root = Tree(4)
    root_right = Tree(3)
    root_left = Tree(1)

    print_tree(root)
