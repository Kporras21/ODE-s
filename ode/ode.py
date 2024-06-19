import numpy as np
import matplotlib.pyplot as plt
import math


def Euler(function, x_0, t, N):
    """Devuelve la solución númerica de una ODE de primer orden no homogenea

    args:
        function (callable) -- La función complementaria de la ODE
        X_0 (float) -- Valor de la función solución en el valor inicial
        t (float) -- Valor de muestreo máximo en el que se hará el cálculo
        N (int) -- cantidad de pasos entre puntos de muestreo

    returns:
        tuple: retorna una tupla (times, x) donde times y x son arrays de la variable independiente y dependiente respectivamente.

    """
    times = np.linspace(0, t, N)
    h = times[1] - times[0]
    x = np.zeros(np.size(times))
    x[0] = x_0
    for i in range(len(times)-1):
        x[i+1]= x[i]+ h * function(x[i], times[i])
    return times, x

def RK2(function, x_0, t, N):
    times = np.linspace(0, t, N)
    h = times[1] - times[0]
    x = np.zeros(np.size(times))
    x[0] = x_0

    for i in range(len(times)-1):
        k1 = h * function(x[i], t[i])
        k2 = h * function(x[i] + k1/2, times[i] + h/2)
        x[i+1] = x[i] + k2
    return x

def RK4(function, x_0, t, N):
    times = np.linspace(0, t, N)
    h = times[1] - times[0]
    x = np.zeros(np.size(times))
    x[0]= x_0

    for i in range (len(times)-1):
        k1 = h * function(x[i], times[i])
        k2 = h * function(x[i] + k1/2, times[i] + h/2)
        k3 = h * function(x[i] + k2, times[i]+h/2)
        k4 = h * function(x[i] + k3, times + h)
        x[i+1]= x[i] + 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return x

def f(x,t):
    return np.sin(t) - x**3

tiempo_euler, Euler_example = Euler(f, 0, 10, 100)

plt.plot(tiempo_euler, Euler_example)
plt.show()