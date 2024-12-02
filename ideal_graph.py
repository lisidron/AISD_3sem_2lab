import math

def avlWorst(x):
    return (1.44*math.log2(x+2))
def avlAv(x):
    return (1.44*math.log2(x))
def avlBest (x):
    return (math.log2(x))

def rbtWorst(x):
    return 2*(math.log2(x+1))
def rbtAv(x):
    return 2*(math.log2(x))
def rbtBest (x):
    return (math.log2(x))

def bstWorst(x):
    return x-1
def bstAv(x):
    return (4.311*math.log2(x))
def bstBest (x):
    return (math.log2(x))