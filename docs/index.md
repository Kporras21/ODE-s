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
\sum\epsilon = \sum_{k=0}^{N-1}\frac{h^2}{2}\left. \frac{d^2x}{dt^2} \right|_{x_{k}, t_{k}} = \frac{h}{2}\sum_{k=0}^{N-1}h\left.\frac{df}{dt}\right|_{x_{k}, t_{k}}\\
\approx \frac{h}2\int_{a}^{b}\frac{df}{dt}d t = \frac{h}{2}\left[f_{b} - f_{a}\right].
$$

donde $N = (b-a)/h$ (cantidad de pasos). 

* El algoritmo toma la siguiente forma:
  - Empezar con $t = t_{0}$, $x = x_{0}$
  - EL tiempo se divide en pasos de tamaño $h$
  - Para cada paso $t_{i}$, se actualiza $x_{i}$ utilizando: $x_{i} = x_{i-1} + hf(x_{i-1})$

## Metodo de Range-Kutta de orden 2 

Este método utiliza el método de Euler evaluado en un punto medio. Es decir, se utiliza el punto medio $t + h/2$. 

Aplicando la expansión de Taylor en dicho punto se obtiene: 

$$
x(t + h) = x\left(t + \frac{h}{2}\right) + \frac{h}{2}\left(\frac{{\rm d}x}{{\rm d}t}\right)_{t+h/2} + \frac{h^2}{8}\left(\frac{{\rm d}^2x}{{\rm d}t^2}\right)_{t+h/2} + O(h^3).
$$

Haciendo lo mismo para $x(t)$ se obtiene: 

$$
x(t) = x\left(t + \frac{h}{2}\right) - \frac{h}{2}\left(\frac{{\rm d}x}{{\rm d}t}\right)_{t+h/2} + \frac{h^2}{8}\left(\frac{{\rm d}^2x}{{\rm d}t^2}\right)_{t+h/2} + O(h^3).
$$

Al sustraer ambas ecuaciones obtenemos

$$
x(t + h) = x(t) + h\left(\frac{{\rm d}x}{{\rm d}t}\right)_{t+h/2} + O(h^3)
$$

Finalmente,

$$
\boxed{x(t + h) = x(t) + hf[x(t + h/2), t + h/2] + O(h^3)}.
$$

por lo tanto, el error es de de orden $h^3$.


Para aproximar el valor de $x(t + h/2)$ se utiliza el método de Euler con un paso $h/2$, $(x + h/2) = x(t) + \frac{h}{2}f(x,t)$. 


* De esta manera, obtenemos las ecuaciones del método RK2:
- $k_1 = hf(x,t),$
- $k_2 = hf\left(x + \frac{k_1}{2},t + \frac{h}{2}\right)$
- $x(t + h) = x(t) + k_2$.

De esta forma, el error global es de orden $O(h^2)$. 

## Método de Range-Kutta de orden 4

El algoritmo de Runge-Kutta de segundo orden se puede aplicar a puntos ubicados $x(t)$ y $x(t + h)$ realizando expansiones de Taylor. El $4^{\rm to}$ orden corresponde al mejor compromiso entre complejidad y error de aproximación.

* El algoritmo toma la siguiente forma:
- $k_1 = hf(x, t)$,
- $k_2 = hf\left(x + \frac{k_1}{2}, t+\frac{h}2\right)$,
- $k_3 = hf\left(x + \frac{k_2}{2}, t+\frac{h}2\right)$,
- $k_4 = hf\left(x + k_3, t + h \right)$,
- $x(t+h) = x(t) + \frac{1}{6}(k_1 + 2 k_2 + 2k_3 + k_4)$

El error de aproximación es del orden $O(h^5)$, mientras que el error global es aproximadamente del orden $O(h^4)$.
    
