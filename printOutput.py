import matplotlib.pyplot as plt
import numpy as np

lim = 20  # The limit of the graph


def print_output(f, root, tol):
    xmin = root - lim
    xmax = root + lim
    x = np.linspace(xmin, xmax, 30)
    y = f(x)
    xlab = 'x'
    ylab = 'y'
    symbol_color = 'r-'

    # Result of the bisection method
    print("Using a tolerance of ", tol, ", Estimate = ", root)
    # Plotting the function
    fig = x_yplot(x, y, xmin, xmax, xlab, ylab, 'f(x)', symbol_color)
    fig = plt.scatter(root, f)
    plt.savefig("Solution.png")
    plt.show()


def x_yplot(x, y, xmin, xmax, xlab, ylab, fig_title, symbol_color):
    fig = plt.figure()
    fig.suptitle(fig_title, fontsize=12)
    plt.plot(x, y, symbol_color)  # plotting the function
    plt.xlim(xmin, xmax)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.grid(True)
    return fig
