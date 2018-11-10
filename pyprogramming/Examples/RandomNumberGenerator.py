import multiprocessing 
import random
import sys

rangeMin = 1
rangeMax = 9

def randomGenerator_Backend(backInput):
    return random.randint(rangeMin, rangeMax)

def randomGenerator(num):
    pool = multiprocessing.Pool()
    return pool.map(randomGenerator_Backend, range(0, num))

randNum = int(sys.argv[1])
print(sys.argv[0], randNum)

random.seed(999)
#randomGenerator(randNum)
