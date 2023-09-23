import MBisection as k
import MNewton as n
import MModified as m
import MSecant as s
import sys
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np


def display_menu():
    """Display the available root-finding methods."""
    print("\nSelect a method to find the root of the function:")
    methods = ["Bisection", "Newton", "Newton's Modified Method", "Secant", "Exit"]
    for index, method in enumerate(methods):
        print(index + 1, method)
    return int(input("\nSelect the method number: "))


def get_root(choice, f, df, ddf):
    """Execute the selected root-finding method."""
    if choice == 1:
        a = float(input("Enter the starting interval a: "))
        b = float(input("Enter the ending interval b: "))
        tol = float(input("Enter the tolerance: "))
        print("\nUsing Bisection method:")
        return k.my_bisection(f, a, b, tol)
    elif choice == 2:
        x0 = float(input("Enter the initial guess x0: "))
        epsilon = float(input("Enter the tolerance: "))
        max_iter = int(input("Enter the maximum number of iterations: "))
        print("\nUsing Newton method:")
        return n.newton(f, df, x0, epsilon, max_iter)
    elif choice == 3:
        x0 = float(input("Enter the initial guess x0: "))
        epsilon = float(input("Enter the tolerance: "))
        max_iter = int(input("Enter the maximum number of iterations: "))
        print("\nUsing Modified Newton-Raphson method:")
        return m.modified(f, df, ddf, x0, epsilon, max_iter)
    elif choice == 4:
        x0 = float(input("Enter the first initial guess x0: "))
        x1 = float(input("Enter the second initial guess x1: "))
        epsilon = float(input("Enter the tolerance: "))
        max_iter = int(input("Enter the maximum number of iterations: "))
        print("\nUsing Secant method:")
        return s.secant(f, x0, x1, epsilon, max_iter)
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        sys.exit()
    else:
        print("Invalid selection. Please try again.")
        return None


def plot_function(f, root=None, xmin=-10, xmax=10):
    x_vals = np.linspace(xmin, xmax, 400)
    y_vals = [f(x) for x in x_vals]
    fig = plt.figure()
    fig.suptitle('Graph of f(x)', fontsize=12)
    plt.plot(x_vals, y_vals, 'b-', label='f(x)')
    if root:
        plt.scatter(root, f(root), color='red', label=f'Root: {root:.5f}')
    plt.xlim(xmin, xmax)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
    return fig


def main():
    """Main function to run the program."""
    x = sp.symbols('x')

    while True:
        user_function = input("\nEnter your function in terms of x (e.g., x**2 - 2): ")
        f_expr = sp.sympify(user_function)
        f = sp.lambdify(x, f_expr, "numpy")
        df_expr = sp.diff(f_expr, x)
        df = sp.lambdify(x, df_expr, "numpy")
        ddf_expr = sp.diff(df_expr, x)
        ddf = sp.lambdify(x, ddf_expr, "numpy")

        user_choice = display_menu()
        root = get_root(user_choice, f, df, ddf)
        if root is not None:
            print(f"The root of the function {user_function} is approximately: {root:.5f}")
            plot_function(f, root)


if __name__ == "__main__":
    main()
