from ModuloNAL import numALetras

while (True):
	numeroStr = input("Ingrese un número del 0 al 9999: ")
	respuesta = numALetras(int(numeroStr))

	if( respuesta == "ERROR"):
		print("Numero fuera de rango. Intente nuevamente.")
	else:
		print("El número ingresado es: " + respuesta + " ("+numeroStr+").")

