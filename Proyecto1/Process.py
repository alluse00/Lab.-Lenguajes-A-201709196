from Objects import *

def OrdenarM(tokens):
    PosR = obtenerRestaurante(tokens)
    rest = restaurant(tokens[PosR].lexema)
    subSec = tokens[PosR + 1:]
    indices = IndicesDM(subSec)
    for i in range(0, len(indices) - 1):
        NSec = subSec[indices[i]].lexema
        sec = section(NSec)
        SubOp = subSec[indices[i] + 2:indices[i + 1]]
        indiceOpciones = IndicesOM(SubOp)
        print(indiceOpciones)
        for j in range(0, len(indiceOpciones) - 1):
            rec = SubOp[indiceOpciones[j]:indiceOpciones[j + 1]]
            subOp = Qs1(rec)
            Op = option(subOp[0].lexema, subOp[1].lexema, subOp[2].lexema, subOp[3].lexema)
            sec.opciones.append(Op)
        rest.secciones.append(sec)
    return rest

def IndicesDM(tokens):
    posSecciones = []
    pos = 0
    for tok in tokens:
        tipoTK = tok.lexema
        if tipoTK != ":":
            pos += 1
        elif tipoTK == ":":
            posSecciones.append(pos-1)
            pos += 1
    posSecciones.append(len(tokens))
    return posSecciones

def IndicesOM(tks):
    posOpciones = []
    pos = 0
    for tok in tks:
        tipoTK = tok.lexema
        if tipoTK != "[":
            pos += 1
        else:
            posOpciones.append(pos)
            pos += 1
    posOpciones.append(len(tks))
    return posOpciones

def Qs1(vector):
    sinSignos = []
    for elemento in vector:
        tipoTK = elemento.tk
        if tipoTK != "Signo":
            sinSignos.append(elemento)
    return sinSignos

def obtenerRestaurante(toks):
    ind = 0
    pos = 0
    for elemento in toks:
        tipoTK = elemento.lexema
        if tipoTK != "=":
            pos += 1
        else:
            ind = pos + 1
    return ind

#-------------------------------------------------------------------

def OrdenarP(tokens):
    datosP = IndicesDP(tokens)
    datos = tokens[:datosP]
    datosS = Qs2(datos)
    print("posicion %")
    print(datosP)
    print(
        f"datos: {datosS[0].lexema} | {datosS[1].lexema} | {datosS[2].lexema} | {datosS[3].lexema} ")
    SubP = tokens[datosP + 1:]
    print("imprimir tokens sub pedidos")
    for sp in SubP:
        print(sp.lexema)
    fact = bill(datosS[0].lexema, datosS[1].lexema, datosS[2].lexema, datosS[3].lexema)
    indices = IndicesOP(SubP)
    print("Indices opciones")
    print(indices)
    for i in range(0, len(indices) - 1):
        sub_pedido = SubP[indices[i]:indices[i + 1]]
        ped_sSig = Qs2(sub_pedido)
        print(f"sub_pedido: {ped_sSig[0].lexema} | {ped_sSig[1].lexema}")
        p = order(ped_sSig[0].lexema, ped_sSig[1].lexema)
        fact.pedidos.append(p)
        p.imprimir()
    return fact

def IndicesDP(tokens):
    pos = 0
    for tok in tokens:
        tipoTK = tok.lexema
        if tipoTK != "%":
            pos += 1
        elif tipoTK == "%":
            return pos
        else:
            return None

def IndicesOP(tks):
    posOpciones = []
    pos = 0
    for tok in tks:
        tipoTK = tok.tk
        if tipoTK == "Numero":
            posOpciones.append(pos)
            pos += 1
        else:
            pos += 1
    posOpciones.append(len(tks))
    return posOpciones

def Qs2(vect):
    signosnt = []
    for elemento in vect:
        tipoTK = elemento.tk
        if tipoTK != "Signo":
            signosnt.append(elemento)
    print("opcion sin signos")
    for sig in signosnt:
        print(sig.lexema)
    return signosnt