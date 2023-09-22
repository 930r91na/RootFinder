import ErrorHandling as errorHandling


def secantMethod(f, x0, x1, tol, max_iter):
    print('Secant Method')
    step = 1
    while True:
        if f(x0) == f(x1):
            # print('Zero division encountered!')
            raise errorHandling.NotSolved("Zero division encountered!")
            break
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print('Iter {}: x = {:.6f}, f(x) = {:.6f}'.format(step, x2, f(x2)))
        x0, x1 = x1, x2
        step += 1
        if step > max_iter:
            raise errorHandling.NotSolved("Maximum iterations reached")
            break
        if abs(f(x2)) <= tol:
            break
    print('Estimated root: {:.8f}'.format(x2))
