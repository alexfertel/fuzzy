import numpy as np
from fuzzy import nodes
from matplotlib import pyplot as plt

def shunting_yard(tokens):
    special = {'(': 2, ')': 2, 'AND': 0, 'OR': 0, 'NOT': 0, 'IS': 1, 'null': -1}

    queue, stack = [], []
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            top = stack[-1] if len(stack) > 0 else 'null'
            while top != '(':
                queue.append(stack.pop())
                top = stack[-1]
            stack.pop()
        elif token in special.keys():
            top = stack[-1] if len(stack) > 0 else 'null'
            while special[top] > special[token] and top != '(' and top == token:
                queue.append(stack.pop())
                if len(stack) > 0:
                    top = stack[-1]
                else:
                    break
            stack.append(token)
        else:
            queue.append(token)

    while len(stack) > 0:
        queue.append(stack.pop())

    return queue

def postfixtoast(postfix):
    special = {'AND', 'OR', 'IS', 'NOT'}

    stack = []
    for token in postfix:
        if token not in special:
            stack.append(nodes.Node(token))
        else:
            if token == "NOT":
                operand = stack.pop()
                node = nodes.UnaryNode(token)
                node.child = operand
                stack.append(node)
            else:
                right = stack.pop()
                left = stack.pop()
                node = nodes.BinaryNode(token)
                node.right = right
                node.left = left
                stack.append(node)

    return stack.pop() if stack else nodes.Node('')



def plot(fns, domain):
    a, b = domain
    x_val = [x for x in np.arange(a, b, .001)]

    for fn in fns:
        y_val = [fn(x) for x in x_val]
        plt.plot(x_val, y_val)

    # plt.savefig(f'paper/images/{name}.png', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    # s = "a IS b AND c IS d OR e IS f"
    # s = "a OR b OR c"
    s = "a AND NOT ( b OR c )"
    print(s)
    postfix = shunting_yard(s.split(' '))
    print(postfix)
    ast = postfixtoast(postfix)
    nodes.preorderprint(ast)
    print()
    nodes.inorderprint(ast)
