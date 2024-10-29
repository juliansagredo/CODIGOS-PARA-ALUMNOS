#=============================
#  Julián T. Becerra Sagredo
#=============================
#  Matemática Algorítmica
#  Paradigmas de Programación
#  ESFM IPN  Septiembre 2024
#=============================

#=============================
#  Importación de módulos
#=============================
import matplotlib.pyplot as grafica
import math

#===========================================
#  Función exponencial con serie de Taylor
#  1 + x + x*x/(2*1) + x*x*x/(3*2*1) + ...
#===========================================
def exponencial(n:int=150,x:float=0.5):
    factorial = 1.0
    exponencial_de_x = 1.0
    x_a_la_n = 1.0
    for i in range(1,n):
       x_a_la_n *= x
       factorial *= float(i)
       s = 1.0/factorial 
       exponencial_de_x += s*x_a_la_n
    return exponencial_de_x

#============================================
#  Función exponencial serie factorizada
#  1 + x*(1 + (x/2)*(1 + (x/3)*(1 + ... )))
#============================================
def exponencial_pro(n:int=150,x:float=0.5):
    flag = False
    if x<0:
        flag = True
        x = -x
    s = 1.0
    for i in range(n,0,-1):
        s *= x/float(i)
        s += 1.0
    if flag == True:
        s = 1/s
    return s

#=====================
#  Programa principal 
#=====================
m = 200       # Puntos totales
serie = 1000  # Sumandos en la serie
error1 = []
error2 = []
x0 = -1.0     # Punto inicial
dx = 0.01     # Distancia entre puntos en la recta
b = list(range(m))
x = [x0+n*dx for n in b]
for i in range(m):
    y = x0+dx*i
    error1.append(exponencial(serie,y)-math.exp(y))
    error2.append(exponencial_pro(serie,y)-math.exp(y))

#===============================================================
#  Gráfica de errores entre nuestra exponencial y la de python
#===============================================================
grafica.subplot(211)
grafica.plot(x,error1)
grafica.subplot(212)
grafica.plot(x,error2)
grafica.show()
