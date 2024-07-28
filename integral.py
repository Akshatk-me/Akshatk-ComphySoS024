import math 

def func(x: float):
    return math.exp(-x*x) # return e^{-x^2}


n = 1000 #step size
a = 0.0
b = 1.0 

h = (b-a)/n 
lsum = 0 

for i in range(0,n):
    x = a + i * h 
    lsum = lsum + func(x)

sum_lower = lsum * h
sum_upper = sum_lower + h*(func(a) - func(b))

print("sum_lower: ", sum_lower, "sum_upper: ", sum_upper) 






