
def newton(f, df, x0, epsilon, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after', n, 'iterations.')
            return xn
        df_xn = df(xn)
        if df_xn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn / df_xn
    print('Exceeded maximum iterations. No solution found.')
    return None