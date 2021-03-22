from Objects import *

def Vect(inicio, final):
    vector = []
    for i in range(inicio, final + 1):
        vector.append(i)
    return vector

def ExistR(pos, txt):
    ID = [32, 61]
    p = ""
    letrasmin = Vect(65, 90)
    letrasmay = Vect(97, 122)
    letras = letrasmin + letrasmay
    while pos < len(txt):
        charCode = ord(txt[pos])
        char = txt[pos]
        if charCode in letras:
            p += char
            pos += 1
        elif charCode in ID:
            if p.lower() == "restaurante":
                return True
            else:
                return False
        else:
            return False

def afdM(ruta):
    signos = [91, 93, 58, 59, 44, 61]
    letrasmin = Vect(65, 90)
    letrasmay = Vect(97, 122)
    letras = letrasmin + letrasmay
    num = Vect(48, 57)
    guionBajo = [95]
    CID = letras + num + guionBajo
    ID = [32, 59]
    TM = []
    err = []
    arr = [TM, err]
    cache = ""
    NoT = 1
    NoE = 1
    tkCorrecto = True
    numD = 0
    with open(ruta, mode="r", encoding="utf-8") as fichero:
        fila = 1
        for linea in fichero.readlines():
            texto = linea.strip("\n")
            estado = 0
            pos = 0
            long = len(texto)
            while pos < long:
                charCode = ord(texto[pos])
                char = texto[pos]
                if estado == 0:
                    if charCode == 32:
                        pos += 1

                    elif charCode in letras:
                        if ExistR(pos, linea) is True:
                            tk = token(NoT, "restaurante", fila, pos, "Palabra Reservada")
                            TM.append(tk)
                            pos += 11
                            NoT += 1
                        else:
                            estado = 1
                            cache += char
                            pos += 1

                    elif charCode in signos:
                        tk = token(NoT, char, fila, pos, "Signo")
                        TM.append(tk)
                        NoT += 1
                        pos += 1

                    elif charCode in num:
                        estado = 3
                        cache += char
                        pos += 1

                    elif charCode == 39:
                        estado = 2
                        pos += 1

                    else:
                        print("error")
                        tkE = tokenE(NoE, char, fila, pos - len(cache), "caracter no valido")
                        err.append(tkE)
                        NoE += 1
                        pos += 1
                        cache = ""

                elif estado == 1:
                    if charCode in CID:
                        cache += char
                        pos += 1
                    elif charCode in ID:
                        tk = token(NoT, cache, fila, pos - len(cache), "Identificador")
                        TM.append(tk)
                        if tkCorrecto is False:
                            tkE = tokenE(NoE, cache, fila, pos - len(cache), "Identicador no valido")
                            err.append(tkE)
                            NoE += 1
                        tkCorrecto = True
                        estado = 0
                        NoT += 1
                        cache = ""
                    else:
                        print(charCode)
                        print(char)
                        print(f"Caracter de identificador desconocido '{char}' error detectado")
                        print(charCode)
                        print(char)
                        cache += char
                        pos += 1
                        tkCorrecto = False

                elif estado == 2:
                    if charCode != 39:
                        cache += char
                        pos += 1

                    else:
                        if cache == "":
                            cache = "Sin Descripcion"
                        tk = token(NoT, cache, fila, pos, "Cadena")
                        TM.append(tk)
                        NoT += 1
                        cache = ""
                        pos += 1
                        estado = 0

                elif estado == 3:
                    if charCode in num:
                        cache += char
                        pos += 1

                    elif charCode == 46:
                        cache += char
                        pos += 1
                        estado = 4

                    elif charCode == 32 or charCode == 59:
                        tk = token(NoT, cache, fila, pos - len(cache), "Numero")
                        TM.append(tk)

                        if tkCorrecto is False:
                            tkE = tokenE(NoE, cache, fila, pos - len(cache), "numero no valido")
                            err.append(tkE)
                            NoE += 1

                        tkCorrecto = True
                        NoT += 1
                        estado = 0
                        cache = ""

                    else:
                        cache += char
                        pos += 1
                        tkCorrecto = False

                elif estado == 4:
                    if charCode in num:
                        cache += char
                        pos += 1
                        numD += 1
                    elif charCode == 32 or charCode == 59:
                        tk = token(NoT, cache, fila, pos - len(cache), "Numero")
                        TM.append(tk)
                        if numD == 0:
                            cache += "0"
                        if tkCorrecto is False:
                            tkE = tokenE(NoE, cache, fila, pos - len(cache), "numero no valido")
                            err.append(tkE)
                            NoE += 1
                        NoT += 1
                        tkCorrecto = True
                        estado = 0
                        numD = 0
                        cache = ""

                    else:
                        pos += 1
                        cache += char
                        tkCorrecto = False

                else:
                    print("error")
                    tkE = tokenE(NoE, char, fila, pos - len(cache), "caracter no valido")
                    err.append(tkE)
                    NoE += 1
                    pos += 1
                    cache = ""
            fila += 1
    return arr
