A = (
	("","","","cero"),
	("mil ","ciento ","diec","uno"),
	("dos mil ","doscientos ","veint","dos"),
	("tres mil ","trecientos ","treinta","tres"),
	("cuatro mil ","cuatrocientos ","cuarenta","cuatro"),
	("cinco mil ","quinientos ","cincuenta","cinco"),
	("seis mil ","seiscientos ","sesenta","seis"),
	("siete mil ","setecientos ","setenta","siete"),
	("ocho mil ","ochocientos ","ochenta","ocho"),
	("nueve mil ","novecientos ","noventa","nueve"),
	)


while(True):
	numeroStr = input("Ingrese un número del 0 al 9999: ")
	numeroInt = int (numeroStr)
	if (numeroInt < 10000 and numeroInt >=0):
		print (numeroInt)
		numeroLetras = ""
		for i in range (4):
			numeroLetras = numeroLetras + A[int(numeroStr[i])][i]
		print(numeroLetras)
	else: 
		print("Numero no correcto. Intente nuevamente.")