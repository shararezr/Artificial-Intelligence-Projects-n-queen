import math

class MyProbability:
    def calculate(self,old_solution,new_solution,T):
        dE = (old_solution-new_solution)/T
        if new_solution < old_solution:
            return 1.0
        return math.exp(dE)