import numpy as np

# Define una medida de complejidad de una función de onda, por ejemplo, la cantidad de picos
def complexity(wave_function):
    peaks = np.sum(wave_function[1:-1] > wave_function[:-2])  # Cuenta los picos
    return peaks

# Implementa un algoritmo greedy para simplificar la función de onda
def simplify_wave_function(wave_function, threshold=0.01):
    current_complexity = complexity(wave_function)
    while True:
        # Intenta reducir la complejidad eliminando pequeños picos
        new_wave_function = np.copy(wave_function)
        for i in range(1, len(wave_function) - 1):
            if wave_function[i] < threshold:
                new_wave_function[i] = (wave_function[i - 1] + wave_function[i + 1]) / 2
        new_complexity = complexity(new_wave_function)
        # Si la nueva función de onda es menos compleja, la actualizamos
        if new_complexity < current_complexity:
            wave_function = new_wave_function
            current_complexity = new_complexity
        else:
            break
    return wave_function

# Ejemplo de uso
original_wave_function = np.array([0, 0.1, 0.5, 0.8, 0.5, 0.1, 0])
simplified_wave_function = simplify_wave_function(original_wave_function)
print("Función de onda original:", original_wave_function)
print("Función de onda simplificada:", simplified_wave_function)
