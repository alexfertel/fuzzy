from fuzzy import membership as m
from fuzzy.rules import Rule
from fuzzy.utils import plot
from fuzzy.aggregations import *
from fuzzy import nodes
from functools import partial
from pprint import pprint


class Fuzzy:
    def __init__(self, inputs, outputs, operators, rules, aggregation_method, defuzzification_method):
        self.inputs = inputs  # variable description in fuzzy sets
        self.outputs = outputs  # variable description in fuzzy sets
        # self.facts = facts  # <variable name, initial value> dict
        self.operators = operators  # Instance of a class deriving BaseOperatorSet
        self.defuzz = defuzzification_method  # Defuzzification method to use
        self.aggreg = aggregation_method  # Aggregation method to use

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
        print("Fuzzy Vectors:", self.fuzzy_vectors)


        # Rule application
        self.clipped = {}
        for vname in self.outputs.keys():
            self.clipped[vname] = {}    
            for sname in self.outputs[vname].sets.keys():
                self.clipped[vname][sname] = []    

        # self.clipped = { vname: { sname: [] for sname in self.outputs[vname].sets.keys() } for vname in self.outputs.keys() }
        for rule in self.rules:
            head_evaluation = self.evaluate(rule.head.ast)
            print("Head Evaluation:", head_evaluation)

            # if type(rule.body.ast) is nodes.BinaryNode:
            outvar = rule.body.ast.left.value
            fuzzy_set = rule.body.ast.right.value
            # else:

            # curried = self.outputs[outvar].fuzzy_sets[fuzzy_set]
            # aggregated = partial(self.aggreg, curried, head_evaluation)

            # self.clipped[outvar][fuzzy_set].append(aggregated)
            self.clipped[outvar][fuzzy_set].append(head_evaluation)

        print("Clipped:", self.clipped)

        # Aggregate
        maxing = {}
        for vname in self.clipped.keys():
            maxing[vname] = []
            for sname, values in self.clipped[vname].items():
                curried = self.outputs[vname].fuzzy_sets[sname]
                aggregated = partial(self.aggreg, curried, max(values))
                maxing[vname].append(aggregated)

            maxing[vname] = partial(aggregate, maxing[vname])

        print("Aggregate", maxing)

        for vname in maxing.keys():
            plot([maxing[vname]], self.outputs[vname].domain)

        # Defuzzify
        crisp_output = maxing.copy()
        for vname in maxing.keys():
            crisp_output[vname] = self.defuzz(self.outputs[vname].domain, maxing[vname])

        return crisp_output

    # def evaluate(self, tree):
    #     if type(tree) is nodes.UnaryNode:
    #         value = self.evaluate(tree.child)
    #         operator = self.operators[tree.value]
    #         return operator.apply(value)
    #     elif type(tree) is nodes.BinaryNode:
    #         operator = self.operators[tree.value]
    #         left = self.evaluate(tree.left)
    #         right = self.evaluate(tree.right)
    #         return operator.apply(left, right)
    #     else:
    #         print(tree)


    def evaluate(self, node):
        if node.value == "IS":
            return self.fuzzy_vectors[node.left.value][node.right.value]

        operator = self.operators[node.value]
        if node.value == "NOT":
            child = self.evaluate(node.child)
            return operator.apply(child)
        else:

            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            result = operator.apply(left, right)
            print("OPERATOR:", node.value, "OPERANDS", left, right, "RESULT:", result)
            return result
            

