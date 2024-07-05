import unittest

from Diferencias_finitas import *

# class TestFiniteDifferenceCalculator(unittest.TestCase):

#     def test_finite_difference(self):
#         def func(x):
#             return np.sin(x)
#         x = np.pi / 4  # 45 grados
#         expected = np.cos(x)
#         result = finite_difference(func, x)
#         self.assertAlmostEqual(result, expected, places=5)

#     def test_symbolic_derivative(self):
#         x = sp.symbols('x')
#         func_expr = sp.sin(x)
#         x_value = np.pi / 4  # 45 grados
#         expected = float(sp.cos(x).subs(x, x_value))
#         result = symbolic_derivative(func_expr, x, x_value)
#         self.assertAlmostEqual(result, expected, places=5)

# if __name__ == '__main__':
#     unittest.main()


def test_comparison():
    x = sp.symbols('x')
    
    # Prueba con sin(x)
    func = np.sin
    func_expr = sp.sin(x)
    x_points = np.linspace(0, 2 * np.pi, 10)
    
    for x_val in x_points:
        numerical_derivative = finite_difference(func, x_val)
        exact_value = symbolic_derivative(func_expr, x, x_val)
        print(f"sin(x) -> x = {x_val:.5f}")
        print(f"Diferencia finita: {numerical_derivative:.5f}")
        print(f"Derivada exacta: {exact_value:.5f}")
        print(f"Error absoluto: {abs(numerical_derivative - exact_value):.5e}")
        print()
    
    # Prueba con cos(x)
    func = np.cos
    func_expr = sp.cos(x)
    
    for x_val in x_points:
        numerical_derivative = finite_difference(func, x_val)
        exact_value = symbolic_derivative(func_expr, x, x_val)
        print(f"cos(x) -> x = {x_val:.5f}")
        print(f"Diferencia finita: {numerical_derivative:.5f}")
        print(f"Derivada exacta: {exact_value:.5f}")
        print(f"Error absoluto: {abs(numerical_derivative - exact_value):.5e}")
        print()

# Llamar a la función de prueba
test_comparison()

def test_varied_functions_and_h():
    x = sp.symbols('x')
    
    functions = [
        (np.sin, sp.sin(x)),
        (np.cos, sp.cos(x)),
        (np.exp, sp.exp(x)),
        (np.log, sp.log(x))
    ]
    
    h_values = [1e-1, 1e-3, 1e-5, 1e-7]
    x_points = np.linspace(1, 10, 5)  # evitar 0 para log(x)

    for func, func_expr in functions:
        print(f"Testing function: {func.__name__}")
        for h in h_values:
            print(f"  Using h = {h}")
            for x_val in x_points:
                numerical_derivative = finite_difference(func, x_val, h)
                exact_value = symbolic_derivative(func_expr, x, x_val)
                print(f"    x = {x_val:.5f}")
                print(f"    Diferencia finita: {numerical_derivative:.5f}")
                print(f"    Derivada exacta: {exact_value:.5f}")
                print(f"    Error absoluto: {abs(numerical_derivative - exact_value):.5e}")
                print()

# Llamar a la función de prueba
test_varied_functions_and_h()

def error_analysis():
    x = sp.symbols('x')
    func = np.sin
    func_expr = sp.sin(x)
    x_val = np.pi / 4  # 45 grados
    h_values = np.logspace(-10, -1, 10)
    
    errors = []
    
    for h in h_values:
        numerical_derivative = finite_difference(func, x_val, h)
        exact_value = symbolic_derivative(func_expr, x, x_val)
        error = abs(numerical_derivative - exact_value)
        errors.append((h, error))
        print(f"h = {h:.1e}, Error absoluto = {error:.5e}")
    
    return errors

# Ejecutar análisis de errores
error_analysis()

import matplotlib.pyplot as plt

def plot_error_analysis(errors):
    h_vals, error_vals = zip(*errors)
    plt.figure()
    plt.loglog(h_vals, error_vals, marker='o')
    plt.xlabel('Paso h')
    plt.ylabel('Error absoluto')
    plt.title('Análisis de Error de Diferencias Finitas')
    plt.show()

# Ejecutar análisis de errores y visualizar
errors = error_analysis()
plot_error_analysis(errors)