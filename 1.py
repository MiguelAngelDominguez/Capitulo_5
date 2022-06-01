import numpy as np
import matplotlib.pyplot as plt
import math

def Bisec(fun, x_a, x_b, steps=10):
    n=0
    x_ant=0
    error_a=0
    valor_v=6.405124837953327
    error_rpv=0
    for n in range(steps+1):
        x_m = (x_a + x_b) / 2
        error_a=(x_m-x_ant)*100 / x_m
        error_v=valor_v-x_m
        error_rpv=(error_v/valor_v)

        if f(x_m) == 0:
            return x_m
        
        if f(x_a) * f(x_m) < 0:
            x_b = x_m
        else:
            x_a = x_m
        x_ant=x_m
    
    return (x_a + x_b) / 2,n,error_a,error_rpv

def raicesEcuacion_2(a,b,c):
    determinate=caso=((b**2)-(4*c*a))**(1/2)
    if(caso>=0):caso="Reales"
    else:caso="Imagianrios"
    x1= (-b+determinate)/(2*a)
    x2= (-b-determinate)/(2*a)
    return x1,x2,determinate,caso

def Graficar_funcion(fx,inicio, parada,semilla=500):
    xi=np.linspace(inicio,parada,semilla)
    fi=fx(xi)
    plt.plot(xi,fi, label='f(x)')
    plt.axhline(0, color='k')
    plt.title('Grafica de Funcion')
    plt.legend()
    plt.show()


print("la ecuacion cuadratica tiene esta forma : ")
print("f(x) = ax^2 + bx + c")
a = -0.5
b = 2.50
c = 4.5
print("________________________________")
print(f"teniendo una forma de : {a}x^2 + {b}x +{c} \n\n")
x1,x2,determinate,caso=raicesEcuacion_2(a,b,c)
print(" - las raices de la ecuacion son ",caso, " , teniendo una determinate de : ",determinate)
print(f" - las raices son : x1 -> {x1}  x2 -> {x2}")

f = lambda x: (a*x**2)+(b*x)+c
Graficar_funcion(f,-50,50)
print("________________________________")
print(" -  por metodo de biseccion :")
x_max,n,error_a,error_rpv=Bisec(f,5,10)
print(f" - para en la iteracion : {n}")
print(f" - x max : {x_max}")
print(f" - error aproximado : {error_a}")
print(f" - error rpv : {error_rpv}")