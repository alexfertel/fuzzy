
class Fuzzy:
    def __init__(self, inputs, outputs, facts, operators, rules):
        self.inputs = inputs  # variable description in fuzzy sets
        self.outputs = outputs  # variable description in fuzzy sets
        self.facts = facts  # <variable name, initial value> dict
        self.operators = operators
        self.rules = rules

    def fuzzify(self):
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

