from ast import Lambda
import numpy as np
import matplotlib.pyplot as plt
import math

def falsaPosicion(funcion, x_a, x_b,error_r=0.001, iteraciones=100):
    x_real=2.666666
    solucion= None
    contador = 0
    error_calculado = 101
    error_rpv=0
    while contador <= iteraciones and error_calculado>error_r:
        contador+=1
        solucion = x_b-((funcion(x_b)*(x_b - x_a))/(funcion(x_b) - funcion(x_a)))
        error_rpv=abs((x_real-solucion)/x_real)
        error_calculado = abs((solucion - x_a)/solucion)
        print(f" - error_a : {error_calculado}")
        print(f" - error_t : {error_rpv}")
        #Se redefine el nuevo intervalo con los signos 
        if funcion(x_a) * funcion(solucion)>=0: 
            x_a = solucion
        else: 
            x_b = solucion 
            
    print('la solucion aproximada es: {:.3f}'.format(solucion))
    print('encontrada en: {:.0f}'.format(contador) + ' iteraciones')

def Graficar_funcion(fx,inicio, parada,semilla=1000):
    xi=np.linspace(inicio,parada,semilla)
    fi=fx(xi)
    plt.plot(xi,fi, label='f(x)')
    plt.axhline(0, color='k')
    plt.title('Grafica de Funcion')
    plt.legend()
    plt.show()


print("la ecuacion cuadratica tiene esta forma : ")
print("f(x) = (ax+b)/x")
a=-0.3
b=0.8
print("________________________________")
print(f"teniendo una forma de : ({a}x+{b})/x \n\n")

print("________________________________")
print(" METODO ANALITICO")
print(" (-0.3x+0.8)/x = 0 ;  x != 0")
print(" -0.3x = -0.8")
print(" x = 2.666 \n\n")

f = lambda x: ((a*x) + b)/x
Graficar_funcion(f,-30,30)

print("________________________________")
print(" - por metodo de la falsa posicion : ")
falsaPosicion(f,1,3,0.03) 