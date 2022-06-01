from ast import Lambda
import numpy as np
import matplotlib.pyplot as plt
import math

#paramtros de entra de la funcion con: la ecuacion, x inicial y final, error , cantidad de iteraciones
def Bisec(fun, x_a, x_b, eps=None, steps=100):    
    for n in range(steps + 1):
        xr=(x_a+x_b)/2
        if(xr!=0):
            ea=abs((x_b-x_a)/(x_b+x_a))
        if (ea<eps):
            return xr
        if f(xr) == 0:
            return xr
        fa=f(x_a)
        fr=f(xr)
        test=fa*fr
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


print("la ecuacion  tiene esta forma : ")
print("f(y) = 1-((q**2)/(g*(3*y+((y**2)/2))**3))*((3+y))")
q=20
g=9.81
print("________________________________")
f = lambda y: 1-((q**2)/(g*(3*y+((y**2)/2))**3))*((3+y))
Graficar_funcion(f,-30,30)
print("________________________________")
print(" -  por metodo de biseccion :")
x=Bisec(f,0.5,2.5,0.01,10)
print(f" - x : {x}")
#se comprueva : 
print(f(x))
