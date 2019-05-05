class Fact:
    def __init__(self, var, value):
        self.var = var
        self.value = value
    
    @staticmethod
    def parse(string):
        tokens = string.strip().split(' ')        
        assert len(tokens) == 3, "A `Fact` must have 3 tokens!"
        return Fact(tokens[0], float(tokens[2]))

    @staticmethod
    def unparse(fact):
        return "".join([fact.var, " IS ", str(fact.value)])

