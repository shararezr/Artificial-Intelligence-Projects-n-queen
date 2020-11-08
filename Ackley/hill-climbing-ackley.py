import random
import math
import matplotlib.pyplot as plt


def ackley(x):
    firstSum = 0.0
    secondSum = 0.0
    for c in x: 
        firstSum += c ** 2.0
        secondSum += math.cos(2.0 * math.pi * c)


    n = float(len(x))
    g = -20.0 * math.exp(-0.2 * math.sqrt(firstSum / n)) - math.exp(secondSum / n) + 20 + math.e
    return g


iteration = 0
resultArray = []

while iteration < 10000:

    initX = (random.uniform(-5, 5) - 0.5) * 0.1
    initY = (random.uniform(-5, 5) - 0.5) * 0.1
    x=[]
    x.append(initX)
    x.append(initY)
    flag = 1

    initAckley = ackley(x)

    productiveStepsCount = 0
    while flag:
        
        newX = (random.uniform(0, 1) - 0.5) * 0.2 + initX
        newY = (random.uniform(0, 1) - 0.5) * 0.2 + initY
        x = []
        x.append(newX)
        x.append(newY)

        newAckley = ackley(x)

        if newAckley < initAckley:
            intitAckley = newAckley
            productiveStepsCount = 0

        else:
            productiveStepsCount += 1
            if productiveStepsCount == 100:
                flag = 0
        initX = newX
        initY = newY	
    print("Iteration " + str(iteration + 1) + " Min Value " + str(initAckley), "x ", initX, " y ", initY)
    resultArray.append(initAckley)
    

    iteration += 1


      
print("minimum of Ackley :" ,min(resultArray))
plt.plot(range(len(resultArray)),resultArray)
plt.show()
    
    
		

      
     
