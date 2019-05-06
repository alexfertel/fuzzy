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

    def infer(self, facts):
        # Fuzzification
        self.fuzzy_vectors = { name: self.inputs[name].fuzzify(value) for name, value in facts } 
        print(self.fuzzy_vectors)

        # Rule application
        for rule in self.rules:
            clause_evaluation = self.evaluate(rule.head)
            
        # Consider if basing rule application on
        # "modus ponens" or "modus tollens"

        # Make aggregation

        # Defuzzify

    def evaluate(self, node):
        if node.value == "IS":
            return self.fuzzy_vectors[node.left.value][node.right.value]
            # for variable in self.inputs:
            #     if variable.name == node.left.value:
            #         variable.sets[node.right.value]()

        left = self.evaluate(node.left)
        right = self.evaluate(node.right)
        operator = self.operators[node.value]
        return operator.apply(left, right)
            

