---
nav_exclude: true
---

# Referencia de API

 Método de Euler 

::: ode.Euler

```python
import numpy as np
import matplotlib.pyplot as plt

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
