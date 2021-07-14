import pyautogui as pa
import ctypes
import cv2
import pytesseract
import keyboard 
import random
import time
from matplotlib import pyplot
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import numpy as np
from PIL import ImageGrab
from functools import partial


ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'	
######################
#Funciones
def obtenerImagenBiance():
	screenshot = pa.screenshot()
	screenshot.save("screenshot.png")
	#screenshot.show()
	return pa.screenshot(region=(690, 195, 140, 35))
	
def stringAfloat(text,Precios):
	global j
	characters = [",","\n"]
	for x in range(len(characters)):
	    text = text.replace(characters[x],"")
	text= text[:8]
	print(text)
	try:
	    	f = float(text)
	    	"""if(i>0):
		    	if ( ( ( ( ( Precios[i-1] - 100) > f ) or ( f > ( (Precios[i-1] + 100) ) ) ) and (Precios[i-1] !=0) ) ):
		    		print("Hubo una anomalidad en el precio regular")
		    		f=Precios[i - 1]"""
	except:
	    print("Hubo un falló, pero es ignorado")
	    if(i>0):
	    	f=Precios[i-1]
	    if(i==0):
	    	f=0;
	    j=j+1
	return f
	
"""def CompraOVenta(Precios,Tiempos):
	#NumeroDeDatosAnteriores=20;
	global SeCompro
	global ventas
	global compras
	global Ganancias
	if(i>100):
		if(SeCompro==0):
				#Si se cumple que el precio viene subiendo a lo largo de 24 segundos y ademas no hay valores muy anomalos entonces se compra
			if(1):
					PreciosCompras.append(Precios[i-1])
					TiemposCompras.append(Tiempos[i-1])
					print("Se realizo una compra")
					plt.scatter(TiemposCompras,PreciosCompras,marker = "o", color= "green")
					compras=compras+1
					SeCompro=1
		if(SeCompro==1):
			if (ventas==0):
				if(1) :
					
					if(1):
							PreciosVentas.append(Precios[i-1])
							TiemposVentas.append(Tiempos[i-1])
							plt.scatter(TiemposVentas,PreciosVentas,marker = "o", color= "red")
							Ganancias = Ganancias + ( (PreciosVentas[ventas] / PreciosCompras[compras - 1]) - 1 )
							ventas=ventas+1
							SeCompro=0
			if (ventas>0):
				if( 1 )
					
					if(1):
							PreciosVentas.append(Precios[i-1])
							TiemposVentas.append(Tiempos[i-1])
							plt.scatter(TiemposVentas,PreciosVentas,marker = "o", color= "red")
							Ganancias = Ganancias + ( (PreciosVentas[ventas] / PreciosCompras[compras - 1]) - 1 )
							ventas=ventas+1
							SeCompro=0
"""

def CompraOVenta2(Precios,Tiempos,Ganancias2,RangoDelPromedio,DeltaPrecioParaVender,DeltaPrecioParaVenderEnCaida):

	Promedio = 0
	global Gan
	global SeCompro2
	global ventas2
	global compras2
	global t1
	Gan=0

	if (i>RangoDelPromedio):
		for k in range(RangoDelPromedio):
			Promedio = Promedio + Precios[i- (k+1)]
		Promedio = Promedio/RangoDelPromedio
	if(i>10):
		if(ventas2==0):
			if(SeCompro2==0):
				if( Precios[i] > Promedio ) :	
							PreciosCompras2.append(Precios[i])
							TiemposCompras2.append(Tiempos[i])
							print("Se realizo una compra2")
							plt.scatter(TiemposCompras2,PreciosCompras2,marker = "o", color= "blue")
							compras2=compras2+1
							SeCompro2=1
		if(ventas2>0):
			if(SeCompro2==0):
				if( ( Precios[i] > Promedio) and ( ( i-t1) > TiempoDeEsperaEntreVentaYCompra) ): #and ( (Precios[i-1]< PreciosVentas2[ventas2-1]) or (Precios[i-2] < PreciosVentas2[ventas2-1]) ) 	
						PreciosCompras2.append(Precios[i])
						TiemposCompras2.append(Tiempos[i])
						print("Se realizo una compra2")
						plt.scatter(TiemposCompras2,PreciosCompras2,marker = "o", color= "blue")
						compras2=compras2+1
						SeCompro2=1
		if(SeCompro2==1):
			if (ventas2==0):
					if ( ( Precios[i] > ( PreciosCompras2[compras2 - 1] + DeltaPrecioParaVender) ) or ( (Precios[i]<Precios[i-1]) and (Precios[i-1]<Precios[i-3] ) ) ) :
							PreciosVentas2.append(Precios[i])
							TiemposVentas2.append(Tiempos[i])
							plt.scatter(TiemposVentas2,PreciosVentas2,marker = "o", color= "yellow")
							Ganancias2.append(Ganancias2[i-1] + ( (PreciosVentas2[ventas2] / PreciosCompras2[compras2-1]) - 1 ))
							SeCompro2=0
							print("Se realizo una Venta2")
							ventas2=ventas2+1
							Gan=1
			if (ventas2>0):
					if ( ( Precios[i] > (PreciosCompras2[compras2 - 1] + DeltaPrecioParaVender) )  or ( Precios[i] < (PreciosCompras2[compras2-1]) - DeltaPrecioParaVenderEnCaida) ) : #or ( (Precios[i]<Precios[i-1]) and (Precios[i-1]<Precios[i-3] ) ) 
							PreciosVentas2.append(Precios[i])
							TiemposVentas2.append(Tiempos[i])
							plt.scatter(TiemposVentas2,PreciosVentas2,marker = "o", color= "yellow")
							Ganancias2.append(Ganancias2[i-1] + ( (PreciosVentas2[ventas2] / PreciosCompras2[compras2-1]) - 1 ))
							SeCompro2=0
							print("Se realizo una Venta2")
							ventas2=ventas2+1
							Gan=1
							t1 = i
	if(Gan==0):
		if (i==0):
			Ganancias2.append(0)
		if(i>0):
			Ganancias2.append(Ganancias2[i-1])




def grafica(frame):
	global i
	GananciasEnUSD=0
	print("Precio")
	screenshot = obtenerImagenBiance()
	text = pytesseract.image_to_string(screenshot,config='--psm 11')
	print('screenshot: ',text)
	if (i>1):
		Precios.append(stringAfloat(text,Precios))
	else:
		Precios.append(stringAfloat(text,Precios))
	Tiempos.append(i)
	#mark = CompraOVenta(Precios,Tiempos)
	mark2 = CompraOVenta2(Precios,Tiempos,Ganancias2,RangoDelPromedio,DeltaPrecioParaVender,DeltaPrecioParaVenderEnCaida)
	print("Tiempo")
	print(i)
	print("Fallos:")
	print(j)
	"""#print("Numero de compras")
	#print(compras)
	#print("Numero de ventas")
	#print(ventas)
	#print("Ganancias:")
	#GananciasEnUSD = Ganancias*100
	#print(GananciasEnUSD)"""
	print("Numero de compras2")
	print(compras2)
	print("Numero de ventas2")
	print(ventas2)
	print("Ganancias2:")
	GananciasEnUSD = Ganancias2[i]*100
	print(GananciasEnUSD)
	line.set_data(Tiempos,Precios)
	fig.gca().relim()
	fig.gca().autoscale_view()
	i=i+1
	GuardarDatos()
	return line,

def GuardarDatos():
	if keyboard.is_pressed('ctrl+e'):
		print("Guardando datos...")
		PvT.append(Tiempos)
		PvT.append(Precios)
		#CvV.append(TiemposCompras2)s
		#CvV.append(TiemposVentas2)
		np.save("DatosPvT",PvT)
		GananciasDatos.append(Tiempos)
		GananciasDatos.append(Ganancias2)
		np.save("DatosGan",GananciasDatos)
		print("No olvides acomodar el archivo de datos!!!")
		exit()

def graficaGan(frame):
	lineGan.set_data(Tiempos,Ganancias2)
	figGan.gca().relim()
	figGan.gca().autoscale_view()
	return lineGan,

############################################


#Programa

i=0
j=0
SeCompro=0
compras=0
ventas=0
Ganancias=0
compras2=0
ventas2=0
SeCompro2=0
Gan=0
t1=0
RangoDelPromedio = 8
DeltaPrecioParaVender = 15
DeltaPrecioParaVenderEnCaida = 5
TiempoDeEsperaEntreVentaYCompra=6

plt.style.use('ggplot')


PvT = []
CvV = []
Tiempos=[]
Precios=[]
PreciosCompras = []
PreciosVentas= []
TiemposVentas = []
TiemposCompras = []
PreciosCompras2 = []
PreciosVentas2= []
TiemposVentas2 = []
TiemposCompras2 = []
Ganancias2=[]
GananciasDatos = []




fig = pyplot.figure(1)
line, = pyplot.plot(Tiempos,Precios,'-')
mark, = pyplot.plot(Tiempos,Precios,'bo')
mark2, = pyplot.plot(Tiempos,Precios,'bo')
figGan = pyplot.figure(2)
lineGan, = pyplot.plot(Tiempos,Ganancias2,'-')
animacion=animation.FuncAnimation(fig,grafica, interval = 1000,)
animacion2=animation.FuncAnimation(figGan,graficaGan, interval = 1000,)

pyplot.show()
#pyplot.show()


###################################




