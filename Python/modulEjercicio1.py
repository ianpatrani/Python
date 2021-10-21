def centenas(numeroInt):
	"Convierte un número de 3 dígitos en palabras"

	A = (
		("","",""),
		("ciento ","diec","un"),
		("doscientos ","veint","dos"),
		("trecientos ","treinta","tres"),
		("cuatrocientos ","cuarenta","cuatro"),
		("quinientos ","cincuenta","cinco"),
		("seiscientos ","sesenta","seis"),
		("setecientos ","setenta","siete"),
		("ochocientos ","ochenta","ocho"),
		("novecientos ","noventa","nueve"),
		)

	
	numeroStr = "{:03d}".format(numeroInt)
	if (numeroInt < 1000 and numeroInt >= 0):
		cifra =(int(numeroStr[0]),int(numeroStr[1]),int(numeroStr[2]))
		numeroLetras=""
		if(cifra[0]==1 and cifra[1]==0 and cifra[2]==0):
			numeroLetras += "cien"
			return numeroLetras;
		else:
			numeroLetras += A[cifra[0]][0]

		if(cifra[1]==1):
			if(cifra[2]==0):
				numeroLetras += "diez"
				return numeroLetras;
			if(cifra[2]==1):
				numeroLetras += "once"
				return numeroLetras;
			if(cifra[2]==2):
				numeroLetras += "doce"
				return numeroLetras;
			if(cifra[2]==3):
				numeroLetras += "trece"
				return numeroLetras;
			if(cifra[2]==4):
				numeroLetras += "catorce"
				return numeroLetras;
			if(cifra[2]==5):
				numeroLetras += "quince"
				return numeroLetras;
		
		elif(cifra[1]==2):
			if(cifra[2]==0):
				numeroLetras += "veinte"
				return numeroLetras;
			

		numeroLetras += A[cifra[1]][1] 
		
		if (A[cifra[1]][1]!=""):
			if(cifra[1]==2 or cifra[1]==1):
				numeroLetras += "i"
			elif(cifra[2]==0):
				numeroLetras +=""
			else:
				numeroLetras += " y "

		numeroLetras += A[cifra[2]][2]
		
		return numeroLetras;
	
	return "ERROR";

def formatearNumero(numeroInt):
	numeroStr=""	
	if((len(str(numeroInt))%3)!=0):
		for i in range (3 - len(str(numeroInt))%3):
			numeroStr += " "
	numeroStr += str(numeroInt)
	numFormat=""
	for i in range(int(len(numeroStr)/3)):
		index=int(len(numeroStr)/3-i-1)
		cent = numeroStr[3*i:3*i+3]			
		numFormat+=cent
		if (index!=0):
			numFormat+=","
	return numFormat.strip();
	
	
def numALetras(numeroInt):

	B = (""," mil "," mill"," mil millones "," bill"," mil billones ",
		" trill"," mil trillones "," cuatrill"," mil cuatrillones ",
		" quintill"," mil quintillones "," sextill"," mil sextillones ",
		" septill"," mil septillones "," octill"," mil octillones "," nonill",
		" mil nonillones "," decill",)

	numeroStr=""	
	if((len(str(numeroInt))%3)!=0):
		for i in range (3 - len(str(numeroInt))%3):
			numeroStr += "0"
	numeroStr += str(numeroInt)
	numeroLetras = ""
	for i in range(int(len(numeroStr)/3)):
		index=int(len(numeroStr)/3-i-1)
		cent = numeroStr[3*i:3*i+3]		
		if( (index%2)==1 and cent[1:3]=="01"):
			numeroLetras += B[index]
		else:
			numeroLetras += centenas(int(cent))+B[index]

		if (index%2==0 and index!=0):
			if (int(cent)==1):
				numeroLetras += "ón "
			else:
				numeroLetras += "ones "

		if(index==0 and cent[2:3]=="1" and cent[1:3]!="11"):
			numeroLetras += "o"

		if(numeroInt==0):
			numeroLetras += "cero"

	return numeroLetras;
