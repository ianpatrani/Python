A = (
    ("", "", "", "cero"),
    ("mil ", "ciento ", "diec", "uno"),
    ("dos mil ", "doscientos ", "veint", "dos"),
    ("tres mil ", "trecientos ", "treinta", "tres"),
    ("cuatro mil ", "cuatrocientos ", "cuarenta", "cuatro"),
    ("cinco mil ", "quinientos ", "cincuenta", "cinco"),
    ("seis mil ", "seiscientos ", "sesenta", "seis"),
    ("siete mil ", "setecientos ", "setenta", "siete"),
    ("ocho mil ", "ochocientos ", "ochenta", "ocho"),
    ("nueve mil ", "novecientos ", "noventa", "nueve"),
)


flag1 = 0
while(True):
    numeroStr = input("Ingrese un número del 0 al 9999: ")
    numeroInt = int(numeroStr)
    numeroStr = "{:04d}".format(numeroInt)
    if (numeroInt < 10000 and numeroInt >= 0):
        cifra = (int(numeroStr[0]), int(numeroStr[1]),
                 int(numeroStr[2]), int(numeroStr[3]))
        print(numeroInt)
        numeroLetras = A[cifra[0]][0]

        if(cifra[1] == 1 and cifra[2] == 0 and cifra[3] == 0):
            numeroLetras = numeroLetras + "cien"
        else:
            numeroLetras = numeroLetras + A[cifra[1]][1]

        if(cifra[2] == 1):
            if(cifra[3] == 0):
                numeroLetras = numeroLetras + "diez"
                flag1 = 1
            if(cifra[3] == 1):
                numeroLetras = numeroLetras + "once"
                flag1 = 1
            if(cifra[3] == 2):
                numeroLetras = numeroLetras + "doce"
                flag1 = 1
            if(cifra[3] == 3):
                numeroLetras = numeroLetras + "trece"
                flag1 = 1
            if(cifra[3] == 4):
                numeroLetras = numeroLetras + "catorce"
                flag1 = 1
            if(cifra[3] == 5):
                numeroLetras = numeroLetras + "quince"
                flag1 = 1
        elif(cifra[2] == 2):
            if(cifra[3] == 0):
                numeroLetras = numeroLetras + "veinte"
                flag1 = 1

        if(flag1 == 0):
            numeroLetras = numeroLetras + A[cifra[2]][2]
            if (A[cifra[2]][2] != ""):
                if(cifra[2] == 2 or cifra[2] == 1):
                    numeroLetras = numeroLetras + "i"
                else:
                    numeroLetras = numeroLetras + " y "

            numeroLetras = numeroLetras + A[cifra[3]][3]

        print(numeroLetras)
        flag1 = 0
    else:
        print("Numero fuera de rango. Intente nuevamente.")
