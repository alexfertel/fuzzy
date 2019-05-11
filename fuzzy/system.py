from fuzzy.fuzzification import fuzzify

class Fuzzy:
    def __init__(self, inputs, outputs, operators, rules):
        self.inputs = inputs
        self.outputs = outputs
        self.operators = operators
        self.rules = rules

    def fuzzify(self, values):
        # Fuzzify each input real-valued variable to obtain
        # the corresponding fuzzy sets describing the "labels"
        # of each variable
        fuzzy_vectors = []
        
        # :param: values is a `list` of `tuples` of the form
        # (variable name, real value)
        for var, value in values:
            # Consider making self.inputs a `dict`
            # fuzzy_vectors.append((var, self.inputs[var].apply(value)))
                        
            for fuzzy_var in self.inputs:
                if var == fuzzy_var:
                    fuzzy_vectors.append((var, fuzzy_var.apply(value)))

        assert len(fuzzy_vectors) == len(values)

        # Consider if basing rule application on
        # "modus ponens" or "modus tollens"

        # Make aggregation

        # Defuzzify

