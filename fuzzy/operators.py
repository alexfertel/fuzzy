class BaseOperator:
    def __init__(self, name, op, fn):
        self.name = name
        self.op = op
        self.fn = fn

    def apply(self, left, right):
        return self.fn(left, right)

class BaseOperatorSet(dict):
    def __init__(self, andop, orop):
        self["and"] = andop
        self["or"] = orop

class MamdaniTNorm(BaseOperator):
    def __init__(self):
        name = "Min"
        op = "And"
        fn = lambda x, y: min(x, y)
        super().__init__(name, op, fn)

class MamdaniTConorm(BaseOperator):
    def __init__(self):
        name = "Max"
        op = "Or"
        fn = lambda x, y: max(x, y)
        super().__init__(name, op, fn)

class Mamdani(BaseOperatorSet):
    def __init__(self):
        andop = MamdaniTNorm()
        orop = MamdaniTConorm()
        super().__init__(andop, orop)
