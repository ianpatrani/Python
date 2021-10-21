from ModuloNAL import numALetras

while (True):
	try:
		numeroStr = input("Ingrese un número del 0 al 9999: ")
		respuesta = numALetras(int(numeroStr))
	except ValueError:
		print("Puso algo que no es un entero. Adios")
		break
	
	if( respuesta == "ERROR"):
		print("Numero fuera de rango. Intente nuevamente.")
	else:
		print("El número ingresado es: " + respuesta + " ("+numeroStr+").")

