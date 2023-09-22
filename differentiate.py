import sympy as sp
from sympy.utilities.lambdify import lambdify

def differentiate(f):
    x = sp.Symbol('x')
    df = sp.diff(f, x)
    df2 = sp.diff(df, x)
    return lambdify(x, df, 'numpy'), lambdify(x, df2, 'numpy')
