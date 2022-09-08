class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


root = Node(10)

root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)


def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)


preorder(root)
inorder(root)
