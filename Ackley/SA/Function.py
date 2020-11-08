from random import uniform
import math

class MyFunction:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.f = lambda x,y: -20.0 * math.exp(-0.2 * math.sqrt((x**2.0+y**2.0) / 2)) - math.exp((math.cos(2.0 * math.pi * x)+math.cos(2.0 * math.pi * y)) / 2) + 20 + math.e

    def calculate(self):
        x,y = {uniform(self.x,self.y),uniform(self.x,self.y)}
        return {'x':x,'y':y,'result':self.f(x,y)}




