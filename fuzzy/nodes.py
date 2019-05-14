class Node:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self)

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
        print(f'{tree.child.value} is only child of {tree.value}')
        preorderprint(tree.child)
        # print(tree)
    elif type(tree) is BinaryNode:
        print(f'{tree.left.value} is left child of {tree.value}')
        preorderprint(tree.left)
        # print(tree)
        print(f'{tree.right.value} is right child of {tree.value}')
        preorderprint(tree.right)
    # else:
        # print(tree)

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
