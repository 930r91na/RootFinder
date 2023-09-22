import numpy as np


def bisectionMeth(f, a, b, epsilon):
    if np.sign(f(a)) == np.sign(f(b)):  # checks if the bounds meet the criteria of a sign change for the theorem
        raise Exception("The scalars a and b do not bound a root")

    m = (a + b) / 2

    if np.abs(f(m)) < epsilon:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return bisectionMeth(f, m, b, epsilon)
    elif np.sign(f(b)) == np.sign(f(m)):
        return bisectionMeth(f, a, m, epsilon)