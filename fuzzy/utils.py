import numpy as np
from fuzzy import nodes
from matplotlib import pyplot as plt

def truncate(curried, value, x):
    y = curried(x)
    return value if value < y else y

def aggregate(functions, x):
    return max(map(lambda fn: fn(x), functions))

def shunting_yard(tokens):
    special = {'(': 2, ')': 2, 'AND': 0, 'OR': 0, 'IS': 1, 'null': -1}

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
            while special[top] >= special[token] and top != '(':
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
    special = {'AND', 'OR', 'IS'}

    stack = []
    for token in postfix:
        if token not in special:
            stack.append(nodes.Node(token))
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
    s = "a IS b AND c IS d OR e IS f"
    print(s)
    postfix = shunting_yard(s.split(' '))
    print(postfix)
    ast = postfixtoast(postfix)
    nodes.preorderprint(ast)
    print()
    nodes.inorderprint(ast)
