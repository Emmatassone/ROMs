import numpy as np
import matplotlib.pyplot as plt

# Define las funciones originales
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

# Definir una función para evaluar el error
def error_function(true_func, approx_func, x_range):
    true_values = true_func(x_range)
    approx_values = approx_func(x_range)
    error = np.mean(np.abs(true_values - approx_values))
    return error

# Definir una función para combinar funciones
def combined_function(functions, x):
    return sum([func(x) for func in functions])

# Inicializar las funciones a utilizar
functions_to_use = [wave_function_1, wave_function_2, wave_function_3, wave_function_4, wave_function_5]

# Iterar hasta que el error sea menor que 10^-12
error_threshold = 1e-12
combined_func = lambda x: 0  # Función inicial vacía
error = np.inf  # Inicializar el error como infinito

while error > error_threshold:
    # Combinar las funciones seleccionadas
    combined_func = lambda x: combined_function(functions_to_use, x)
    
    # Calcular el error
    x_range = np.linspace(-5, 5, 1000)
    true_function = wave_function_1  # Selecciona una función original para calcular el error
    error = error_function(true_function, combined_func, x_range)
    
    # Imprimir el error en cada iteración
    print("Error:", error)
    
    # Agregar la función con el menor error al conjunto de funciones a usar
    best_func = min(functions_to_use, key=lambda f: error_function(true_function, lambda x: combined_function([f], x), x_range))
    functions_to_use.remove(best_func)

# Graficar el resultado
plt.figure(figsize=(10, 6))
plt.plot(x_range, true_function(x_range), label='Función Original')
plt.plot(x_range, combined_func(x_range), label='Función Simplificada')
plt.title('Comparación de la función original y la función simplificada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
