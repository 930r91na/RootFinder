import numpy as np

def modified (f, Df, Df2, x0, epsilon, max_iter):
    xn=x0
    for n in range (0, max_iter):
        fxn=f(xn)
        if abs(fxn)<epsilon:
            print("Found a solution after", n, "iterations")
            return xn
        Dfxn=Df(xn)
        Df2xn=Df2(xn) 
        denominador= Dfxn**2-fxn*Df2xn
        if denominador == 0:
            print("Can't be divided, denominator equals to 0")
            return None
        xn=xn-fxn*Dfxn/denominador
    print("Exceeded maximum iterations. No solution found")
    return None


