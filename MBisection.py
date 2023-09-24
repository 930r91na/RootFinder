import numpy as np
import warnings

def my_bisection(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception ("The scalars a and b do not bound a root")
    m = (a + b) /2
    if np.abs(f(m))<tol:
        return m
    elif np.sign(f(a)) == np.sign(f (m)):
        return my_bisection(f, m, b, tol) 
    elif np.sign(f(b)) == np.sign (f (m)):
        return my_bisection(f, a, m, tol)
    else:
        print("Error. No root found. Try different bounds.")


