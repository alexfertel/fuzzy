from fuzzy.rules import Rule

class Fuzzy:
    def __init__(self, inputs, outputs, facts, operators, rules):
        self.inputs = inputs  # variable description in fuzzy sets
        self.outputs = outputs  # variable description in fuzzy sets
        self.facts = facts  # <variable name, initial value> dict
        self.operators = operators  # Instance of a class deriving BaseOperatorSet
        
        # List of strings representing rules of the form:
        # IF <clause> THEN <clause>
        # where <clause> is of the form:
        # <var_name> IS <fuzzy_set> [<operator> <clause>]
        # where <operator> is one of {`AND`, `OR`}
        # and square brackets indicate optional. 
        self.rules = [Rule.parse(rule) for rule in rules]


    def infer(self):
        fuzzy_vectors = []
        
        for var, value in self.facts:
            # Consider making self.inputs a `dict`
            fuzzy_vectors.append((var, self.inputs[var].apply(value)))
                        
            # for fuzzy_var in self.inputs:
            #     if var == fuzzy_var:
            #         fuzzy_vectors.append((var, fuzzy_var.apply(value)))

        print(fuzzy_vectors)

        # Consider if basing rule application on
        # "modus ponens" or "modus tollens"

        # Make aggregation

        # Defuzzify

