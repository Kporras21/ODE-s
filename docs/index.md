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
\sum\epsilon = \sum_{k=0}^{N-1}\frac{h^2}{2}\left. \frac{d^2x}{dt^2} \right|_{x_k, t_k} = \frac{h}{2}\sum_{k=0}^{N-1}h\left.\frac{df}{dt}\right|_{x_k, t_k}\\
\approx \frac{h}2\int_a^b\frac{df}{dt}d t = \frac{h}{2}\left[f_b - f_a\right].
$$

donde $N = (b-a)/h$ (cantidad de pasos). 

* El algoritmo toma la siguiente forma:
  - Empezar con $t = t\_0$, $x = x\_0$
  - Discretizar el tiempo en pasos temporales de forma equidistante con espaciamiento $h$, donde cada punto en el tiempo está denotado con $t\_i$
  - Para cada punto en el tiempo encontrar $x$ utilizando el resultado de la iteración previa: $x\_i = x_{i-1} + hf(x_{i-1})$

## Metodo de Range-Kutta de orden 2 



## Método de Range-Kutta de orden 4



$$ PV = NRT $$
    
