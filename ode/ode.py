import numpy as np
import matplotlib.pyplot as plt
import math
from typing import Tuple

def Euler(function, x_0, t, N):
    """Devuelve la solución númerica de una ODE de primer orden no homogenea

    Args:
        function (callable): La función complementaria de la ODE
        x_0 (float): Valor de la función solución en el valor inicial
        t (float): Valor de muestreo máximo en el que se hará el cálculo
        N (int): Cantidad de pasos entre puntos de muestreo

    Returns:
        tuple: Retorna una tupla (times, x) donde times y x son arrays de la variable independiente y dependiente respectivamente.
    Example:
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        Se define una función cualquiera que dependa de la variable dependiente y de la variable independiente.
        >>> def f(x,t):
            return np.sin(t) - x**3
        Al introducirla a nuestra función, junto con los parametros deseados, está devuelve la tupla de arrays, lo cual luego podemos plotear.
        >>> tiempo_euler, Euler_example = Euler(f, x_0 = 0, t = 10, N = 100)
        >>> plt.plot(tiempo_euler, Euler_example)
        >>> plt.show()

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
        k1 = h * function(x[i], times[i])
        k2 = h * function(x[i] + k1/2, times[i] + h/2)
        x[i+1] = x[i] + k2
    return x

def RK4(function, x_0, t, N):
    """Devuelve la solución númerica de una ODE de primer orden no homogenea

    Args:
        function (callable): La función complementaria de la ODE
        x_0 (float): Valor de la función solución en el valor inicial
        t (float): Valor de muestreo máximo en el que se hará el cálculo
        N (int): Cantidad de pasos entre puntos de muestreo

    Returns:
        float: Retorna los valores de x que son solucion de la EDO utilizando el metodo de Runge-Kutta de orden 4 




    """
    times = np.linspace(0, t, N)
    h = times[1] - times[0]
    x = np.zeros(np.size(times))
    x[0] = x_0

    for i in range(len(times)-1):
        k1 = h * function(x[i], times[i])
        k2 = h * function(x[i] + k1/2, times[i] + h/2)
        k3 = h * function(x[i] + k2/2, times[i] + h/2)
        k4 = h * function(x[i] + k3, times[i] + h)
        x[i+1] = x[i] + (1/6) * ( k1 + 2 * k2  * k3 + k4) 
    return x 

def f(x,t):
    return np.sin(t) - x**3

tiempo_euler, Euler_example = Euler(f, 0, 10, 100)

plt.plot(tiempo_euler, Euler_example)
plt.show()
