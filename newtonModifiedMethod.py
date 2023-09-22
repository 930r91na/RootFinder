
def newtonModified(f, df, df2, x0, epsilon, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after', n, 'iterations.')
            return xn
        dfxn = df(xn)
        df2xn = df2(xn)
        denom  = ((dfxn)**2 - (fxn * df2xn))
        if denom == 0:
            print('Denominator is equal to zero. No solution was found.')
            return None
        xn = xn - (fxn * dfxn)/denom
    print('Exceeded maximum iterations. No solution found.')
    return None

