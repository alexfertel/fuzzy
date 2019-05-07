class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class UnaryNode(Node):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.child = None

class BinaryNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.left = None
        self.right = None

def preorderprint(tree):
    if type(tree) is UnaryNode:
        preorderprint(tree.child)
        print(tree)
    elif type(tree) is BinaryNode:
        preorderprint(tree.left)
        print(tree)
        preorderprint(tree.right)
    else:
        print(tree)

def inorderprint(tree):
    if type(tree) is UnaryNode:
        preorderprint(tree.child)
        print(tree)
    elif type(tree) is BinaryNode:
        print(tree)
        inorderprint(tree.left)
        inorderprint(tree.right)
    else:
        print(tree)
