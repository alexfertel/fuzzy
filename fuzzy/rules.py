from fuzzy import utils

class Clause:
    def __init__(self, operations):
        self.operations = operations
        self.postfix = utils.shunting_yard(operations)
        self.ast = utils.postfixtoast(self.postfix)

    @staticmethod
    def parse(string):
        tokens = string.strip().split(' ')
        return Clause(tokens)

    @staticmethod
    def unparse(clause):
        return ' '.join(clause.operations)


class Rule:
    def __init__(self, head, body):
        self.head = Clause.parse(head)
        self.body = Clause.parse(body)

    @staticmethod
    def parse(string):
        head, body = string.strip().replace('IF', '').split('THEN')
        return Rule(head, body)

    @staticmethod
    def unparse(rule):
        return ''.join(['IF ', Clause.unparse(rule.head), ' THEN ', Clause.unparse(rule.body)])
