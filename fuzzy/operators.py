class BaseOperator:
    def __init__(self, name, op, fn):
        self.name = name
        self.op = op
        self.fn = fn

    def apply(self, *args):
        return self.fn(*args)

class BaseOperatorSet(dict):
    def __init__(self, andop=None, orop=None, notop=None, isop=None):
        self["AND"] = andop
        self["OR"] = orop
        self["NOT"] = notop
        self["IS"] = istop

class DefaultTNorm(BaseOperator):
    def __init__(self):
        name = "Min"
        op = "And"
        fn = lambda x, y: min(x, y)
        super().__init__(name, op, fn)

class DefaultTConorm(BaseOperator):
    def __init__(self):
        name = "Max"
        op = "Or"
        fn = lambda x, y: max(x, y)
        super().__init__(name, op, fn)

class DefaultComplement(BaseOperator):
    def __init__(self):
        name = "Complement"
        op = "Not"
        fn = lambda x: 1 - x
        super().__init__(name, op, fn)

class DefaultComplement(BaseOperator):
    def __init__(self):
        name = "Complement"
        op = "Not"
        fn = lambda x: 1 - x
        super().__init__(name, op, fn)

class Default(BaseOperatorSet):
    def __init__(self):
        andop = DefaultTNorm()
        orop = DefaultTConorm()
        notop = DefaultComplement()
        super().__init__(andop, orop, notop)
