import sys
import sympy as sp
from sympy import *

import ErrorHandling as errorHandling
import differentiate as diff
import bisectionMethod as bM
import newtonMethod as nM
import newtonModifiedMethod as nMM
import secantMethod as sM
import printOutput as pO


def askFunction():
    print("\nIt is time to introduce your function f in terms of x:\n")

    expression = input("\nInsert your function: ")
    try:
        f = sp.sympify(expression)
        return f
    except sp.SympifyError:
        raise errorHandling.InvalidInput("Invalid input. Please enter a valid mathematical expression.")


def menu():
    ans = True
    while ans:
        print("-----Menu-----")
        print("1) Bisection method \n2) Newton's method \n3) Newton's modified method \n4) Secant method \n5) Exit")

        # take input from user
        ans = input("Choose an option from the Menu shown below: \n")

        # type cast into integer
        ans = int(ans)

        if ans == 1:
            print("Bisection Method\n")
            f = askFunction()
            a = int(input("Type the left end of the interval, value of a: "))
            b = int(input("Type the right end of interval (a,b), in fact, give the value of b: "))
            tol = float(input("Type the tolerance: "))
            root = bM.bisectionMeth(lambdify('x', f), a, b, tol)
            pO.print_output(lambdify('x', f), root, tol)

        elif ans == 2:
            print("Newton's Method\n")
            f = askFunction()
            f_prime = diff.differentiate(f)
            x0 = float(input("Enter the initial guess x0: "))
            tol = float(input("Enter the tolerance level: "))
            max_iter = int(input("Enter the maximum number of iterations: "))
            root = nM.newton(lambdify('x', f), f_prime, x0, tol, max_iter)
            pO.print_output(lambdify('x', f), root, tol)

        elif ans == 3:
            print("Newton's Modified Method\n")
            f = askFunction()
            f_prime, f_biprime = diff.differentiate(f)
            x0 = float(input("Enter the initial guess x0: "))
            tol = float(input("Enter the tolerance level: "))
            max_iter = int(input("Enter the maximum number of iterations: "))
            root = nMM.newtonModified(lambdify('x', f), f_prime, f_biprime, x0, tol, max_iter)
            pO.print_output(lambdify('x', f), root, tol)

        elif ans == 4:
            print("Secant Method\n")
            f = askFunction()
            x0 = float(input("Enter the initial guess x0: "))
            x1 = float(input("Enter a second zero guess x1: "))
            tol = float(input("Enter the tolerance level: "))
            max_iter = int(input("Enter the maximum number of iterations: "))
            root = sM.secantMethod(lambdify('x', f), x0, x1, tol, max_iter)
            pO.print_output(lambdify('x', f), root, tol)

        elif ans == 5:
            sys.exit("Bye")
        else:
            print("Invalid choice. Please enter one of the options shown above")
