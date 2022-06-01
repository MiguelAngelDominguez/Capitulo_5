import numpy as np
import matplotlib.pyplot as plt
import math

def Bisec(fun, x_a, x_b, steps=100):
    n=0
    x_ant=0
    error_a=1
    error_s=0.1
    for n in range(steps+1):
        x_m = (x_a + x_b) / 2
        print(" - x_m: ", x_m)
        print(" - x_ant : ", x_ant)

        if (error_a<error_s):
            return x_m,n,error_a

        if(x_m!=0):
            error_a=abs((x_b-x_a)/(x_b+x_a))
        print("error actual : ",error_a)
        print("error s : ",error_s)
        
        if f(x_m) == 0:
            return x_m,n,error_a     
        if f(x_a) * f(x_m) < 0:
            x_b = x_m
        else:
            x_a = x_m
        x_ant=x_m
    return (x_a + x_b) / 2,n,error_a

def Graficar_funcion(fx,inicio, parada,semilla=500):
    xi=np.linspace(inicio,parada,semilla)
    fi=fx(xi)
    plt.plot(xi,fi, label='f(x)')
    plt.axhline(0, color='k')
    plt.title('Grafica de Funcion')
    plt.legend()
    plt.show()


print("la ecuacion cuadratica tiene esta forma : ")
print("f(x) = ax^3 + bx^2 + cx + d")
a = 5
b = -5
c = 6
d = -2
print("________________________________")
print(f"teniendo una forma de : {a}x^3 + {b}x^2 +{c}x + {d} \n\n")

f = lambda x: (a*x**3)+(b*x**2)+(c*x)+d
Graficar_funcion(f,-50,50)
print("________________________________")
print(" -  por metodo de biseccion :")
x_min,n,error_a=Bisec(f,0,1)
print(f" - para en la iteracion : {n}")
print(f" - x min : {x_min}")
