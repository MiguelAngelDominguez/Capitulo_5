from ast import Lambda
import numpy as np
import matplotlib.pyplot as plt
import math

def falsaPosicion(funcion, x_a, x_b, iteraciones=100, error_r=0.001):
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
print("f(x) =ax^4 + bx^3 + cx^2 + dx + e")
a = 1
b = -8
c = -35
d = 450
e = -1001
print("________________________________")
print(f"teniendo una forma de : {a}x^4 + {b}x^3 + {c}x^2 + {d}x + {e}  \n\n")

f = lambda x: (a*x**4)+(b*x**3)+(c*x**2)+(d*x)+(e)
Graficar_funcion(f,-100,100)

print("________________________________")
print(" - por metodo de la falsa posicion : ")
falsaPosicion(f,4.5,6,5,0.01)