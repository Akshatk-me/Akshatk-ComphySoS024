import math 

def func(x: float):
    return math.exp(-x*x) # return e^{-x^2}


n = 60 #step size
a = 0.0
b = 1.0 

h = (b-a)/n 
tsum = (func(a) + func(b))/2

for i in range(1,n):
    x = a + i * h 
    tsum = tsum + func(x)

tsum = tsum * h 

print("tsum: ", tsum)






