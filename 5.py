from ast import Lambda
import numpy as np
import matplotlib.pyplot as plt
import math

def Bisec(fun, x_a, x_b, eps=None, steps=100):    
    for n in range(steps + 1):
        xr=(x_a+x_b)/2
        if(xr!=0):
            ea=abs((x_b-x_a)/(x_b+x_a))
        if (ea<eps):
            return xr
        if f(xr) == 0:
            return xr
        
        test=f(x_a)*f(xr)
        if test < 0:
            x_b = xr
        elif test>0 :
            x_a = xr
        else:
            ea=0
        
    return xr

def Graficar_funcion(fx,inicio, parada,semilla=1000):
    xi=np.linspace(inicio,parada,semilla)
    fi=fx(xi)
    plt.plot(xi,fi, label='f(x)')
    plt.axhline(0, color='k')
    plt.title('Grafica de Funcion')
    plt.legend()
    plt.show()


print("la ecuacion cuadratica tiene esta forma : ")
print("f(x) =sen(x) + x^2")
print("________________________________")
f = lambda x: np.sin(x)-x**2
Graficar_funcion(f,-100,100)

print("________________________________")
print(" - por metodo de Biseccion : ")
x=Bisec(f,0.5,1,0.02)
print(" - x : ",x)
print("________________________________")
print(" - replasamos el x encontrado : ")
print(" - ",f(x))