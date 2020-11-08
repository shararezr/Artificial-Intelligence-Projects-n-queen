from Function import MyFunction
from SimulatedAnnealing import SimulatedAnnealing
from Probability import MyProbability
import matplotlib.pyplot as plt


myfun = MyFunction(-10,10)

"""
parameter = Temperature,Minimum Temperature,koefisien,length of itenary each temperatur,Function,Probability
"""


sA = SimulatedAnnealing(1.0,0.0001,0.99,100,myfun,MyProbability())


solution,result = sA.getSolution()
print("Best Solution")
print(solution)
print("length of iteration",len(result))

"""grafik all solution"""
plt.plot(range(len(result)),result)
plt.show()
