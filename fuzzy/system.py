from fuzzy.rules import Rule
from fuzzy import nodes
from functools import reduce


class Fuzzy:
    def __init__(self, inputs, outputs, operators, rules):
        self.inputs = inputs  # variable description in fuzzy sets
        self.outputs = outputs  # variable description in fuzzy sets
        # self.facts = facts  # <variable name, initial value> dict
        self.operators = operators  # Instance of a class deriving BaseOperatorSet
        
        # List of strings representing rules of the form:
        # IF <clause> THEN <clause>
        # where <clause> is of the form:
        # <var_name> IS <fuzzy_set> [<operator> <clause>]
        # where <operator> is one of {`AND`, `OR`}
        # and square brackets indicate optional. 
        self.rules = [Rule.parse(rule) for rule in rules]


    def fuzzify(self, facts):
        fuzzy_vectors = {var: } 
        

    def infer(self, facts):
        fuzzy_vectors = []
        for rule in rules:
            clause_evaluation = self.evaluate(rule.head)
                
                
                # fuzzy_vectors.append((var, self.inputs[var].apply(value)))



                # for fuzzy_var in self.inputs:
                #     if var == fuzzy_var:
                #         fuzzy_vectors.append((var, fuzzy_var.apply(value)))

        print(fuzzy_vectors)

        # Consider if basing rule application on
        # "modus ponens" or "modus tollens"

        # Make aggregation

        # Defuzzify

    def evaluate(self, node):
        if type(node) is nodes.BinaryNode:
            if node.value == "IS":
                for variable in self.inputs:
                    if variable.name == node.left.value:
                        variable.sets[node.right.value]()


            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            operator = self.operators[node.value]
            return operator.apply(left, right)
        else:
            

