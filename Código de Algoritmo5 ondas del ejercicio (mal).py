import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones de onda
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

# Definir una medida de complejidad de una función de onda
def complexity(wave_function):
    peaks = np.sum(wave_function[1:-1] > wave_function[:-2])
    return peaks

# Implementar un algoritmo greedy para simplificar la función de onda
def simplify_wave_function(wave_function, threshold=0.01):
    current_complexity = complexity(wave_function)
    while True:
        new_wave_function = np.copy(wave_function)
        for i in range(1, len(wave_function) - 1):
            if wave_function[i] < threshold:
                new_wave_function[i] = (wave_function[i - 1] + wave_function[i + 1]) / 2
        new_complexity = complexity(new_wave_function)
        if new_complexity < current_complexity:
            wave_function = new_wave_function
            current_complexity = new_complexity
        else:
            break
    return wave_function

# Generar puntos en el eje x
x = np.linspace(-10, 10, 1000)

# Calcular los valores de las funciones de onda originales para los puntos en x
y1 = wave_function_1(x)
y2 = wave_function_2(x)
y3 = wave_function_3(x)
y4 = wave_function_4(x)
y5 = wave_function_5(x)

# Simplificar las funciones de onda con diferentes valores de threshold
threshold_values = [0.01, 0.05, 0.1]  # Ejemplos de diferentes valores de threshold

plt.figure(figsize=(10, 6))

for i, threshold in enumerate(threshold_values):
    y1_simplified = simplify_wave_function(y1, threshold=threshold)
    y2_simplified = simplify_wave_function(y2, threshold=threshold)
    y3_simplified = simplify_wave_function(y3, threshold=threshold)
    y4_simplified = simplify_wave_function(y4, threshold=threshold)
    y5_simplified = simplify_wave_function(y5, threshold=threshold)
    
    plt.subplot(len(threshold_values), 1, i + 1)
    plt.plot(x, y1_simplified, label=f'f1 (threshold={threshold})')
    plt.plot(x, y2_simplified, label=f'f2 (threshold={threshold})')
    plt.plot(x, y3_simplified, label=f'f3 (threshold={threshold})')
    plt.plot(x, y4_simplified, label=f'f4 (threshold={threshold})')
    plt.plot(x, y5_simplified, label=f'f5 (threshold={threshold})')
    plt.title(f'Funciones de onda simplificadas (threshold={threshold})')
    plt.xlabel('x')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()
