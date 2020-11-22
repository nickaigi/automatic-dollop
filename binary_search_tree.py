class Tree(object):
    def __init__(self, x):
        self.value = x
        self.right = None
        self.left = None

def inorder(root):
    """
    Inorder BST traversal:
        1. Traverse the left subtree: inorder(left)
        2. Visit the root
        3. Traverse the right subtree: inorder(right)
    """
    import pdb; pdb.set_trace()
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def postorder(root):
    """
    Postorder BST traversal:
        1. Traverse left subtree: postorder(left)
        2. Traverse left subtree: postorder(left)
        3. Visit the root
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)


def preorder(root):
    """
    Preorder BST traversal:
        1. visit the root
        2. Traverse left subtree: preorder(left)
        3. Traverse right subtree: preorder(right)
    """
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

if __name__ == '__main__':
    root = Tree(4)
    root_right = Tree(3)
    root_left = Tree(1)

    inorder(root)
