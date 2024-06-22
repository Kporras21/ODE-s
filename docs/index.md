# Métodos númericos para la resolución de ODE´s no homogeneas de primer orden

Se analizára y explicará la implementación de los metodos númericos de Euler, Runge-Kutta de orden 2 y Runge-Kutta de orden 4 mediante codigo de Python. 

## Método de Euler

Según la definición de expansión de Taylor para una función $x(t)$ en el punto $t+h$ se tiene que:
 
$$
\text{Expansión Taylor} \Rightarrow x(t+h) = x(t) + h\frac{dx}{dt} + \overbrace{ \frac{h^2}{2} \frac{d^2x}{dt^2} } ^{\epsilon} + O(h^3).
$$

en donde suponemos $h$ lo suficientemente pequeño. Ello implica que la función en el punto $t+h$ se puede escribir como:

$$
\boxed{x(t + h) = x(t) + hf(x,t).}
$$

El error dependerá del número de pasos utilizados y, por lo tanto, de $h$. Se representa de la siguiente manera:  

$$
\sum\epsilon = \sum_{k=0}^{N-1}\frac{h^2}{2}\left. \frac{d^2x}{dt^2} \right|\_{x\_k, t\_k} = \frac{h}{2}\sum_{k=0}^{N-1}h\left.\frac{df}{dt}\right|\_{x\_k, t\_k}\\
\approx \frac{h}2\int\_a^b\frac{df}{dt}d t = \frac{h}{2}\left[f\_b - f\_a\right].
$$

donde $N = (b-a)/h$ (cantidad de pasos). 

* El algoritmo toma la siguiente forma:
  - Empezar con $t = t\_0$, $x = x\_0$
  - EL tiempo se divide en pasos de tamaño $h$
  - Para cada paso $t\_i$, se actualiza $x\_i$ utilizando: $x\_i = x_{i-1} + hf(x_{i-1})$

## Metodo de Range-Kutta de orden 2 



## Método de Range-Kutta de orden 4

El algoritmo de Runge-Kutta de segundo orden se puede aplicar a puntos ubicados $x(t)$ y $x(t + h)$ realizando expansiones de Taylor. El $4^{\rm to}$ orden corresponde al mejor compromiso entre complejidad y error de aproximación.

* El algoritmo toma la siguiente forma:
- $k\_1 = hf(x, t)$,
- $k\_2 = hf\left(x + \frac{k\_1}{2}, t+\frac{h}2\right)$,
- $k\_3 = hf\left(x + \frac{k\_2}{2}, t+\frac{h}2\right)$,
- $k\_4 = hf\left(x + k\_3, t + h \right)$,
- $x(t+h) = x(t) + \frac{1}{6}(k\_1 + 2 k\_2 + 2k\_3 + k\_4)$

El error de aproximación es del orden $O(h^5)$, mientras que el error global es aproximadamente del orden $O(h^4)$.
    
