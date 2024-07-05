import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def finite_difference(f, x, h=1e-5):
    """
    Aproximar la derivada de la función f en el punto x usando diferencias finitas.
    
    Args:
    f (function): Función a derivar.
    x (float): Punto en el cual evaluar la derivada.
    h (float): Paso para diferencias finitas.
    
    Returns:
    float: Aproximación de la derivada.
    """
    return (f(x + h) - f(x - h)) / (2 * h)\
    
def func(x):
    return np.sin(x)

def exact_derivative(x):
    return np.cos(x)

def compare_derivatives(f, df_exact, x_vals, h=1e-5):
    """
    Compara la derivada numérica con la derivada exacta en una lista de puntos.
    
    Args:
    f (function): Función a derivar.
    df_exact (function): Derivada exacta de la función.
    x_vals (list): Lista de puntos en los cuales evaluar las derivadas.
    h (float): Paso para diferencias finitas.
    
    Returns:
    None
    """
    for x in x_vals:
        numerical_derivative = finite_difference(f, x, h)
        exact_value = df_exact(x)
        print(f"x = {x:.5f}")
        print(f"Diferencia finita: {numerical_derivative:.5f}")
        print(f"Derivada exacta: {exact_value:.5f}")
        print(f"Error absoluto: {abs(numerical_derivative - exact_value):.5e}")
        print()

x_points = np.linspace(0, 2 * np.pi, 10)
compare_derivatives(func, exact_derivative, x_points)

def symbolic_derivative(func_expr, symbol, x_value):
    """
    Calcula la derivada simbólica de una función en un punto dado.
    
    Args:
    func_expr (sympy expression): Expresión simbólica de la función.
    symbol (sympy symbol): Variable simbólica.
    x_value (float): Punto en el cual evaluar la derivada.
    
    Returns:
    float: Valor de la derivada en el punto dado.
    """
    derivative_expr = sp.diff(func_expr, symbol)
    return float(derivative_expr.subs(symbol, x_value))

x = sp.symbols('x')
func_expr = sp.sin(x)
x_points = np.linspace(0, 2 * np.pi, 10)

for x_val in x_points:
    numerical_derivative = finite_difference(np.sin, x_val)
    exact_value = symbolic_derivative(func_expr, x, x_val)
    print(f"x = {x_val:.5f}")
    print(f"Diferencia finita: {numerical_derivative:.5f}")
    print(f"Derivada exacta: {exact_value:.5f}")
    print(f"Error absoluto: {abs(numerical_derivative - exact_value):.5e}")
    print()