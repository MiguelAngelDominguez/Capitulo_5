from ast import Lambda
import numpy as np
import matplotlib.pyplot as plt
import math

def falsaPosicion(funcion, x_a, x_b, error_r=0.001 , iteraciones=100):
    # Se inicializan las variables 
    x_real = 5.60979
    solucion= None
    contador = 0
    error_calculado = 101
    #Se evalua si la raiz esta dentro del intervalo
    if funcion(x_a) * funcion(x_b) <= 0:
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
        print('con un error de:{:.3f}'.format(error_calculado) + '%' )
    else:
        print('no existe solucion en ese intervalo')


def Graficar_funcion(fx,inicio, parada,semilla=1000):
    xi=np.linspace(inicio,parada,semilla)
    fi=fx(xi)
    plt.plot(xi,fi, label='f(x)')
    plt.axhline(0, color='k')
    plt.title('Grafica de Funcion')
    plt.legend()
    plt.show()


print("la ecuacion cuadratica tiene esta forma : ")
print("f(x) = ax^3.5 + b = 0")
a = 1
b = -80
print("________________________________")
print(f"teniendo una forma de : {a}x^3.5 + {b} \n\n")
print("________________________________")
print(" - Solucion Analitica : ")
print(" - x^3.5 - 80 = 0")
print(" - x^3.5 = 80 ")
print(" - x^(7/2) = 80 ")
print(" - x = 80 ^ (2/7)")
print(" - x = 6400^(1/7)")
print(" - x = 3.497")
f = lambda x: (a*x**(3.5)) + b
Graficar_funcion(f,-100,100)

print("________________________________")
print(" - por metodo de la falsa posicion : ")
falsaPosicion(f,2,5,0.025)