class Operator:
    def __init__(self, name, op, fn)
        self.name = name
        self.op = op
        self.fn = fn

    def apply(self, left, right):
        return self.fn(left, right)

# comparison = Operator("comparison", "IS", lambda x, y: x == y)

class Condition:
    def __init__(self, left, op, right)
        self.left = left
        self.op = op
        self.right = right

    @staticmethod
    def parse(string):
        head, body = string.lower().strip().split('then').replace('if', '')
        return Rule(head, body)

    @staticmethod
    def unparse():
        return ''.join(['IF ', self.head, ' THEN ', self.body])


class Rule:
    def __init__(self, head, body)
        self.head = head
        self.body = body

    @staticmethod
    def parse(string):
        head, body = string.lower().strip().split('then').replace('if', '')
        return Rule(head, body)

    @staticmethod
    def unparse():
        return ''.join(['IF ', self.head, ' THEN ', self.body])
                

