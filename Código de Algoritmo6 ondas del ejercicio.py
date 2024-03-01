import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import optuna
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Generar datos de ejemplo
np.random.seed(42)
X = np.random.randn(1000, 10)
y = np.random.randint(0, 2, 1000)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir la función de objetivo para Optuna
def objective(trial):
    n_estimators = trial.suggest_int('n_estimators', 10, 100)
    max_depth = trial.suggest_int('max_depth', 2, 32, log=True)
    clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=0)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)

# Ejecutar la optimización de hiperparámetros con Optuna
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)

print('Best trial:')
trial = study.best_trial
print('Accuracy:', trial.value)
print("Params:", trial.params)

# Entrenar y evaluar el modelo con los mejores hiperparámetros
best_params = trial.params
clf = RandomForestClassifier(**best_params, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
