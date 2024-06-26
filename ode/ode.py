import numpy as np
import matplotlib.pyplot as plt
import math
from typing import Tuple

def Euler(function, x_0, t, N) -> Tuple[np.ndarray, np.ndarray]:
    """Devuelve la solución númerica de una ODE de primer orden no homogenea utilizando el método de Euler.

    Example:

        >>> import numpy as np
        >>> import math
        >>> def function1(x,t):
                return np.sin(t) - x**3
        >>> result1 = Euler(function2, x_0 = 0, t = 10, N = 20)
        >>> print(result1)
        [ 0.        ,  0.        ,  0.26439534,  0.71189381,  1.04830651,
        0.89488942,  0.77464602,  0.52141013,  0.17502349, -0.28921312,
        -0.80263945, -0.97897518, -0.73458315, -0.50879969, -0.16038526,
        0.30726691,  0.81787725,  0.97386719,  0.72957635,  0.49945695]

        >>> import numpy as np
        >>> import math
        >>> def function2(x,t):
                return np.cos(t) - np.exp(x)
        >>> result2 = Euler(function2, x_0 = 0, t = 10, N = 20)
        >>> print(result2)
        [ 0.          0.         -0.07122963 -0.30068299 -0.69461108 -1.22547997
        -1.83935079 -2.44923905 -2.94540698 -3.22627014 -3.23429889 -2.97958585
        -2.54286684 -2.05822057 -1.67919565 -1.53173235 -1.6669454  -2.0490437
        -2.5843312  -3.14972638]

        >>> import numpy as np
        >>> import math
        >>> def function3(x,t):
                return np.sinh(t) - x
        >>> result3 = Euler(function3, x = 0, t = 10, N = 20)
        >>> print(result2)
        [0.00000000e+00 0.00000000e+00 2.89975549e-01 7.99505019e-01
        1.60072764e+00 2.88651558e+00 5.00512012e+00 8.54940181e+00
        1.45203906e+01 2.46089117e+01 4.16738619e+01 7.05521213e+01
        1.19429399e+02 2.02160465e+02 3.42196400e+02 5.79232069e+02
        9.80458092e+02 1.65960684e+03 2.80919126e+03 4.75507497e+03]


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
    """Devuelve la solución númerica de una ODE de primer orden no homogenea utilizando el método de RK2.

    Example:

        >>> import numpy as np
        >>> import math
        >>> def function1(x,t):
                return np.sinh(t) - x
        >>> result3 = Euler(function1, x = 0, t = 10, N = 20)
        >>> print(result2)
        [0.00000000e+00 1.40108316e-01 4.69503675e-01 1.02355156e+00
        1.92379318e+00 3.40367390e+00 5.86937546e+00 1.00116836e+01
        1.69997981e+01 2.88115312e+01 4.87931927e+01 8.26076821e+01
        1.39839426e+02 2.36711025e+02 4.00681647e+02 6.78230589e+02
        1.14803236e+03 1.94325791e+03 3.28932352e+03 5.56778776e+03]


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
        k1 = h * function(x[i], times[i])
        k2 = h * function(x[i] + k1/2, times[i] + h/2)
        x[i+1] = x[i] + k2
    return times, x

def RK4(function, x_0, t, N):
    """Devuelve la solución númerica de una ODE de primer orden no homogenea utilizando el método de RK4.

    Example:

        >>> import numpy as np
        >>> import math
        >>> def function1(x,t):
                return np.sin(t) - x**3
        >>> result1 = RK4(function1, x_0 = 0, t = 10, N = 20)
        >>> print(result1)
        [ 0.          0.13505937  0.48487586  0.81979626  0.93102462  0.88144889
        0.72370945  0.46026479  0.06848691 -0.42773679 -0.78084333 -0.83096351
        -0.6993985  -0.43991777 -0.04506765  0.45089026  0.79057875  0.83047637
        0.69376603  0.43014634]

        >>> def falling_function(v, t):
                k = 0.1       
                m = 1.0       
                return 9.8 - (k / m) * v
        >>> result2 = RK4(function_falling, x_0 = 0, t = 10, N = 20)
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
        >>> result3 = RK4(rc_circuit_function, x = 0, t = 10, N = 20)
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
        times_x tuple: Retorna una tupla (times, x) donde times y x son arrays de la variable independiente y dependiente respectivamente.
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


def function1(x,t):
        return np.sinh(t) - x
times_e, x_e = RK2(function1, 0, 10, 20)
print(x_e)

plt.plot(times_e, x_e)
plt.show()
