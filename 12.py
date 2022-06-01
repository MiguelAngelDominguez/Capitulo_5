from ast import Lambda
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

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


print("la ecuacion tiene esta forma : ")
print("f(x) = ax^6 + bx^4 + cx + d")
a= -2
b= -1.5
c= 10
d= 2
print("________________________________")
print(f"teniendo una forma de : {a}x^6 + {b}x^4 + {c}x + {d} \n\n")

f = lambda x: a*6*x**5 + b*4*x**3 + c
print(" - nos piden el punto maximo entre 0 - 1, para \n lo cual derivamos")
print(" dx : ")
print("f'(x) = -12 x^(5)-1.5*4 x^(3)+10")
print("________________________________")
Graficar_funcion(f,-30,30)
print("________________________________")
print(" -  por metodo de biseccion :")
x=Bisec(f,0,1,0.05)
# print(f" - para en la iteracion : {n}")
print(f" - x : {x}")
