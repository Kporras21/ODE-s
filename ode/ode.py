import numpy as np
import matplotlib.pyplot as plt
import math
from typing import tuple

def Euler(function, x_0, t, N):
    """Devuelve la solución númerica de una ODE de primer orden no homogenea

    Args:
        function (callable): La función complementaria de la ODE
        x_0 (float): Valor de la función solución en el valor inicial
        t (float): Valor de muestreo máximo en el que se hará el cálculo
        N (int): Cantidad de pasos entre puntos de muestreo

    Returns:
        tuple: Retorna una tupla (times, x) donde times y x son arrays de la variable independiente y dependiente respectivamente.


Para asegurarte de que el ejemplo en tu docstring se muestre correctamente como código en la documentación generada con MkDocs y mkdocstrings, puedes intentar los siguientes pasos:

1. Revisar la Docstring
Primero, revisa que la docstring de tu función esté correctamente formateada con la indentación adecuada y los bloques de código encerrados en triple comillas ("""). Aquí hay una versión corregida de tu función Euler:

python
Copy code
# ode.py

import numpy as np
import matplotlib.pyplot as plt

def Euler(function, x_0, t, N):
    """
    Devuelve la solución númerica de una ODE de primer orden no homogenea.

    Args:
        function (callable): La función complementaria de la ODE.
        x_0 (float): Valor de la función solución en el valor inicial.
        t (float): Valor de muestreo máximo en el que se hará el cálculo.
        N (int): Cantidad de pasos entre puntos de muestreo.

    Returns:
        tuple: Retorna una tupla (times, x) donde times y x son arrays de la variable independiente y dependiente respectivamente.

    Example:
        ```python
        import numpy as np
        import matplotlib.pyplot as plt

        def f(x, t):
            return np.sin(t) - x**3

        tiempo_euler, Euler_example = Euler(f, x_0=0, t=10, N=100)
        plt.plot(tiempo_euler, Euler_example)
        plt.xlabel('Tiempo')
        plt.ylabel('Solución')
        plt.title('Ejemplo de solución ODE con método de Euler')
        plt.grid(True)
        plt.show()
        ```
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
        (times, x) tuple: Retorna una tupla (times, x) donde times y x son arrays de la variable independiente y dependiente respectivamente.
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
    return times, x

def f(x,t):
    return np.sin(t) - x**3

tiempo_euler, Euler_example = Euler(f, 0, 10, 100)

plt.plot(tiempo_euler, Euler_example)
plt.show()
