from fuzzy import utils

class Clause:
    def __init__(self, operations):
        self.operations = operations
        self.postfix = utils.shunting_yard(operations)
        self.ast = utils.postfixtoast(self.postfix)

    @staticmethod
    def parse(string):
        special = ["AND", "IS", "OR", "NOT", "(", ")"]
        tokens = string.strip().split(' ')

        changed = True
        while changed:
            changed = False
            result = []
            i = 0
            while i < len(tokens):
                if i == len(tokens) - 1:
                    result.append(tokens[i])
                    break
                if tokens[i] not in special and tokens[i + 1] not in special:
                    result.append(' '.join([tokens[i], tokens[i + 1]]))
                    changed = True
                    result.extend(tokens[i + 2:])
                    break
                else:
                    result.append(tokens[i])
                i += 1
            # print("New")
            # print(tokens)
            # print(result)
            tokens = result.copy() if changed else tokens

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
