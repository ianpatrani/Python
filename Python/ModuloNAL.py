def numALetras(numeroInt):
	"Convierte un número de 4 dígitos en palabras"

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


	numeroStr = "{:04d}".format(numeroInt)
	if (numeroInt < 10000 and numeroInt >= 0):
		cifra =(int(numeroStr[0]),int(numeroStr[1]),int(numeroStr[2]),int(numeroStr[3]))
		
		numeroLetras =	A[cifra[0]][0] 
		
		if(cifra[1]==1 and cifra[2]==0 and cifra[3]==0):
			numeroLetras = numeroLetras + "cien"
			return numeroLetras;

		else:
			numeroLetras = numeroLetras + A[cifra[1]][1]

		if(cifra[2]==1):
			if(cifra[3]==0):
				numeroLetras = numeroLetras + "diez"
				return numeroLetras;
			if(cifra[3]==1):
				numeroLetras = numeroLetras + "once"
				return numeroLetras;
			if(cifra[3]==2):
				numeroLetras = numeroLetras + "doce"
				return numeroLetras;
			if(cifra[3]==3):
				numeroLetras = numeroLetras + "trece"
				return numeroLetras;
			if(cifra[3]==4):
				numeroLetras = numeroLetras + "catorce"
				return numeroLetras;
			if(cifra[3]==5):
				numeroLetras = numeroLetras + "quince"
				return numeroLetras;
		
		elif(cifra[2]==2):
			if(cifra[3]==0):
				numeroLetras = numeroLetras + "veinte"
				return numeroLetras;
			

		numeroLetras = numeroLetras + A[cifra[2]][2] 
		
		if (A[cifra[2]][2]!=""):
			if(cifra[2]==2 or cifra[2]==1):
				numeroLetras = numeroLetras+ "i"
			else:
				numeroLetras = numeroLetras+ " y "

		numeroLetras = numeroLetras + A[cifra[3]][3]
		
		return numeroLetras;
	
	return "ERROR";
