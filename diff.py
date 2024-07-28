import math
imax = 0
imin = 0
n = 30
h = 1 
emax = 0.0
emin = 1
error = 0.0 
x = 0.5

for i in range(1,n):
    h = h/4
    y = (math.sin(x+h) - math.sin(x))/h
    error = abs(math.cos(x) - y)
    print("h: ", h, "y: ", y, "error: ", error)

    if error > emax: 
        emax = error
        imax = i
    if error < emin:
        emin = error 
        imin = i
    
print("emax: ", emax,"imax: ", imax)
print("emin: ", emin,"imin: ", imin)

