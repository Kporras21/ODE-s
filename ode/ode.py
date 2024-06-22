import numpy as np
import matplotlib.pyplot as plt
import math
from typing import Tuple

def Euler(function, x_0, t, N) -> Tuple[np.ndarray, np.ndarray]:
    """Devuelve la solución númerica de una ODE de primer orden no homogenea

    Examples:


    Args:
        function (callable): La función complementaria de la ODE
        x_0 (float): Valor de la función solución en el valor inicial
        t (float): Valor de muestreo máximo en el que se hará el cálculo
        N (int): Cantidad de pasos entre puntos de muestreo

    Returns:
        times_X (Tuple): Retorna un times, x donde times y x son arrays de la variable independiente y dependiente respectivamente.


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

    Example:

        >>> import numpy as np
        >>> import math
        >>> def function1(x,t):
                return np.sin(t) - x**3
        >>> result1 = RK4(function2, 0, 10, 20)
        >>> print(result1)
        [ 0.          0.13505937  0.48487586  0.81979626  0.93102462  0.88144889
        0.72370945  0.46026479  0.06848691 -0.42773679 -0.78084333 -0.83096351
        -0.6993985  -0.43991777 -0.04506765  0.45089026  0.79057875  0.83047637
        0.69376603  0.43014634]
        >>> def falling_function(v, t):
                k = 0.1       
                m = 1.0       
                return 9.8 - (k / m) * v
        >>> result2 = RK4(function_falling, 0, 10, 20)
        >>> print(result2)
        [ 0.          5.02963768  9.80140324 14.32851792 18.62352509 22.69832502
        26.56420785 30.23188487 33.7115182  37.01274893 40.14472385 43.1161208
        45.93517269 48.60969034 51.14708409 53.55438434 55.83826107 58.00504226
        60.06073146 62.01102441]
        >>> def rc_circuit_function(Q, t):
                V = 10.0     
                R = 1.0      
                C = 1.0      
                return (V - Q / C) / R
        >>> result3 = RK4(rc_circuit_function, 0, 10, 20)
        >>> print(result3)
        [0.         4.08913375 6.50616602 7.93484147 8.77931241 9.2784679
        9.57351202 9.74790866 9.85099218 9.91192347 9.94793914 9.96922752
        9.9818108  9.98924861 9.993645   9.99624364 9.99777967 9.99868759
        9.99922425 9.99954147]

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
        x[i+1] = x[i] + (1/6) * (k1 + 2 * k2 + 2  * k3 + k4) 
    return times, x

def f(x,t):
    return np.sin(t) - x**3

tiempo_euler, Euler_example = Euler(f, 0, 10, 100)

plt.plot(tiempo_euler, Euler_example)
plt.show()
