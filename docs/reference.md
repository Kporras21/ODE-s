---
nav_exclude: true
---

# Referencia de API

 Método de Euler 

::: ode.Euler

```python
import numpy as np
import matplotlib.pyplot as plt

def Euler(function, x_0, t, N):

    times = np.linspace(0, t, N)
    h = times[1] - times[0]
    x = np.zeros(np.size(times))
    x[0] = x_0
    for i in range(len(times)-1):
        x[i+1] = x[i] + h * function(x[i], times[i])
    return times, x

# Ejemplo de uso de la función Euler
def f(x, t):
    return np.sin(t) - x**3

tiempo_euler, Euler_example = Euler(f, x_0=0, t=10, N=100)

plt.figure(figsize=(8, 5))
plt.plot(tiempo_euler, Euler_example, label='Solución numérica')
plt.xlabel('Tiempo')
plt.ylabel('Solución')
plt.title('Ejemplo de solución de ODE con método de Euler')
plt.grid(True)
plt.legend()
plt.show()
```
 Método de Runge-Kutta de Segundo Orden (RK2) 

::: ode.RK2

 Método de Runge-Kutta de Cuarto Orden (RK4) 

::: ode.RK4 
