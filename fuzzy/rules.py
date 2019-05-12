class Operation:
    def __init__(self, name, op, fn):
        self.name = name
        self.op = op
        self.fn = fn

    def apply(self, left, right):
        return self.fn(left, right)

# comparison = Operator("comparison", "IS", lambda x, y: x == y)

class Clause:
    def __init__(self, operations):
        self.operations = operations



class Rule:
    def __init__(self, head, body):
        self.head = head
        self.body = body

    @staticmethod
    def parse(string):
        head, body = string.lower().strip().split('then').replace('if', '')
        return Rule(head, body)

    @staticmethod
    def unparse():
        return ''.join(['IF ', self.head, ' THEN ', self.body])
                

