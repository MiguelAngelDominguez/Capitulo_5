from ast import Lambda
import numpy as np
import matplotlib.pyplot as plt
import math


def falsaPosicion(funcion, x_a, x_b,error_r=0.001, iteraciones=100):
    # Se inicializan las variables 
    solucion= None
    contador = 0
    error_calculado = 101
    while contador <= iteraciones and error_calculado>error_r:
        contador+=1
        solucion = x_b-((funcion(x_b)*(x_b - x_a))/(funcion(x_b) - funcion(x_a)))
        error_calculado = abs((solucion - x_a)/solucion)*100
        #Se redefine el nuevo intervalo con los signos 
        if funcion(x_a) * funcion(solucion)>=0: 
            x_a = solucion
        else: 
            x_b = solucion 
            
    print('la solucion aproximada es: {:.3f}'.format(solucion))
    print('encontrada en: {:.0f}'.format(contador) + ' iteraciones')
    print('con un error de:{:.3f}'.format(error_calculado) + '%' )

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
r=3
v=30

print("________________________________")
f = lambda h: (np.pi*r*h**2)-((np.pi*h**3)/3)-v
Graficar_funcion(f,-30,30)

print("________________________________")
print(" - por metodo de la falsa posicion : ")
falsaPosicion(f,0,2,0.01,2)
