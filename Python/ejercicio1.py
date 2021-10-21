from modulEjercicio1 import *

while (True):
	try:
		numeroStr = input("Ingrese un número o 'salir' para terminar: ")
		if(numeroStr=="salir"):
			print("Vuelva pronto!!")
			break
		respuesta = numALetras(int(numeroStr))
	except:
		print("\nError. Sólo números enteros. Intente nuevamente.")
		print("Escriba 'salir' para irse.")
		continue

	if( respuesta == "ERROR"):
		print("Error en la conversión. Intente nuevamente.")
	else:
		print("El número ingresado es: " + respuesta )
		print("( " +formatearNumero(int(numeroStr))+" )")

