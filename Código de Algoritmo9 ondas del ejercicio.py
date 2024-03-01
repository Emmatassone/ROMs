import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones de onda originales
def wave_function_1(x):
    return np.exp(-x*x/2) * np.sin(x*0.99*2*np.pi)

def wave_function_2(x):
    return np.exp(-x*x/2) * np.sin(x*0.09*2*np.pi)

def wave_function_3(x):
    return np.exp(-x*x/2) * np.sin(x*0.21*2*np.pi)

def wave_function_4(x):
    return np.exp(-x*x/2) * np.sin(x*0.35*2*np.pi)

def wave_function_5(x):
    return np.exp(-x*x/2) * np.sin(x*0.85*2*np.pi)

# Definir la función para calcular el error total
def total_error(approx_wave_functions, original_wave_functions, x):
    total_err = 0
    for approx_wave, original_wave in zip(approx_wave_functions, original_wave_functions):
        total_err += np.sum((approx_wave(x) - original_wave(x))**2)
    return total_err

# Definir el algoritmo greedy
def greedy_algorithm(original_wave_functions, epsilon, x):
    approx_wave_functions = original_wave_functions.copy()
    curr_error = total_error(approx_wave_functions, original_wave_functions, x)
    while curr_error > epsilon:
        max_err_reduction = 0
        func_to_remove = None
        for i, wave_func in enumerate(approx_wave_functions):
            new_approx_wave_functions = approx_wave_functions.copy()
            del new_approx_wave_functions[i]
            new_error = total_error(new_approx_wave_functions, original_wave_functions, x)
            err_reduction = curr_error - new_error
            if err_reduction > max_err_reduction:
                max_err_reduction = err_reduction
                func_to_remove = i
        if func_to_remove is not None:
            del approx_wave_functions[func_to_remove]
            curr_error -= max_err_reduction
        else:
            break
    return approx_wave_functions, curr_error

# Parámetros
epsilon = 1e-12
x_values = np.linspace(-5, 5, 100)

# Almacenar las bases obtenidas y los errores correspondientes
bases = []
errors = []

# Ejecutar el algoritmo hasta que el error total sea menor que epsilon
original_wave_functions = [wave_function_1, wave_function_2, wave_function_3, wave_function_4, wave_function_5]
while True:
    approx_wave_functions, total_err = greedy_algorithm(original_wave_functions, epsilon, x_values)
    bases.append(approx_wave_functions)
    errors.append(total_err)
    print(f"Base encontrada con error total: {total_err}")
    if total_err < epsilon:
        break

# Imprimir las bases obtenidas y sus errores
print("\nBases obtenidas:")
for i, base in enumerate(bases):
    print(f"Iteración {i+1}:")
    for wave_func in base:
        print(wave_func.__name__)
    print(f"Error total: {errors[i]}")


# Función para graficar las funciones de onda
def plot_wave_functions(original_wave_functions, approx_wave_functions, x_values):
    plt.figure(figsize=(10, 6))
    for original_wave_func in original_wave_functions:
        plt.plot(x_values, original_wave_func(x_values), label=original_wave_func.__name__)
    for approx_wave_func in approx_wave_functions:
        plt.plot(x_values, approx_wave_func(x_values), linestyle='--', label=approx_wave_func.__name__ + ' (approx)')
    plt.xlabel('x')
    plt.ylabel('Amplitud')
    plt.title('Funciones de onda originales y aproximadas')
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para graficar la evolución del error total
def plot_error_evolution(errors):
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(errors)+1), errors, marker='o', linestyle='-')
    plt.xlabel('Iteración')
    plt.ylabel('Error total')
    plt.title('Evolución del error total durante el algoritmo')
    plt.grid(True)
    plt.show()

# Graficar las funciones de onda originales y aproximadas
plot_wave_functions(original_wave_functions, bases[-1], x_values)

# Graficar la evolución del error total
plot_error_evolution(errors)
