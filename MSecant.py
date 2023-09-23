def secant(f, x0, x1, epsilon, max_iter):
    if abs(f(x0)) < epsilon:
        return x0
    if abs(f(x1)) < epsilon:
        return x1
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:  # Evita la división por cero
            print("Division by zero encountered. Try different initial guesses.")
            return None
        x_temp = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        if abs(f(x_temp)) < epsilon:  # Verifica si la solución es lo suficientemente cercana a cero
            return x_temp
        x0, x1 = x1, x_temp
    print("Exceeded maximum iterations. No solution found within the given tolerance.")
    return None

