from ast import Lambda
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


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
    print('con un error de:{:.3f}'.format(error_calculado) )

def Graficar_funcion(fx,inicio, parada,semilla=1000):
    xi=np.linspace(inicio,parada,semilla)
    fi=fx(xi)
    plt.plot(xi,fi, label='f(x)')
    plt.axhline(0, color='k')
    plt.title('Grafica de Funcion')
    plt.legend()
    plt.show()


print("la ecuacion tiene esta forma : ")
print("v = g*m/cr*(1-exp(-cr/m*tf))")
g=9.8
cr=15
v=35
tf=9
print("________________________________")

f = lambda m: (g*m/cr)*(1-np.e**((-cr/m)*tf))-v
print(" - tomaremos puntos entre 50 y 70")
print("________________________________")
Graficar_funcion(f,-30,30)

print("________________________________")
print(" - por metodo de la falsa posicion : ")
falsaPosicion(f,50,70,0.01)
print(" - remplazando : ")
print(f(59.841)+v)