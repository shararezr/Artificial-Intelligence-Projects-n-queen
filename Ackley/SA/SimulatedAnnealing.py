from random import random

class SimulatedAnnealing:
    def __init__(self,T,min_T,cooling_rate,length,Function,Probability):
        self.T = T
        self.min_T = min_T
        self.cooling_rate = cooling_rate
        self.length = length
        self.Function = Function
        self.Probability = Probability

    def getSolution(self):
        plot = []
        T = self.T
        min_T = self.min_T
        cooling_rate = self.cooling_rate
        length = self.length
        current_state = best_so_far = self.Function.calculate()
        best_so_far["T"] = T
        print("initial")
        print(current_state)
        plot.append(current_state['result'])
        while T > min_T:
            i = 1
            while i <= length:
                new_state = self.Function.calculate()
                plot.append(new_state['result'])
                if new_state['result'] < current_state['result'] :
                  #  print('add best so far')
                    best_so_far = new_state
                    best_so_far["T"] = T
                    print("best-so-far",best_so_far,"T :  ", T )
                ap = self.Probability.calculate(current_state['result'],new_state['result'],T)
                if ap > random():
                   # print('now become current')
                    current_state = new_state
                i += 1

            T = T * cooling_rate
        return best_so_far,plot

