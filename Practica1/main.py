from tkinter import *
from tkinter.filedialog import askopenfilename

cm = []
def abrirDoc():
    root = Tk()
    name = askopenfilename()
    root.withdraw()
    return name
def leerDoc(doc):
    with open(doc) as fichero:
        for lineas in fichero.readlines():
            cm.append(lineas)
        pass
def QuitarComa(lista):
    palabra = []
    for a in lista.split(","):
        palabra.append(a)
    return palabra
def QuitarLineas(vec):
    b = []
    for fil in vec:
        b.append(fil.strip("\n").split("="))
    for fila in b:
        elemento = fila[1]
        orden = fila[1].find("ORDENAR")
        busca = fila[1].find("BUSCAR")
        if busca != -1 & orden == -1:
            fin = fila[1].find("BUSCAR")
            fila.append("BUSCAR")
            numero = ''.join(elemento[:fin - 1].strip().split())
            buscado = ''.join(elemento[fin + 6:].strip().split())
            fila[1] = numero
            fila.append(buscado)
        elif orden != -1 & busca == -1:
            fin = fila[1].find("ORDENAR")
            fila.append("ORDENAR")
            numero = ''.join(elemento[:fin - 1].strip().split())
            fila[1] = numero
        elif orden != -1 & busca != -1:
            fin = fila[1].find("ORDENAR")
            fila.append("ORDENAR")
            numero = ''.join(elemento[:fin - 1].strip().split())
            instrucciones = elemento[fin:].strip()
            fila[1] = numero
            indice = instrucciones.find("BUSCAR")
            fila.append("BUSCAR")
            fila.append(''.join(instrucciones[indice + 6:].strip().split()))
    return b
def Busqueda(vec, num):
    posicion = []
    for i in range(0, (len(vec) - 1)):
        if vec[i] == num:
            posicion.append(i)
    return posicion
def Vacio(a):
    if a:
        return False
    else:
        return True
def Ordenados():
    print("******Listas Ordenadas******")
    for linea in cm:
        for elemento in linea:
            if elemento == "ORDENAR":
                nombreLinea = linea[0]
                numero = QuitarComa(linea[1])
                num = ','.join(sorted(numero))
                print(nombreLinea + ": ORDENADOS = " + num, end="\n")
def Buscados():
    print("*******Listas Buscadas******")
    for linea in cm:
        for elemento in linea:
            if elemento == "BUSCAR":
                nombre = linea[0]
                numero = QuitarComa(linea[1])
                buscado = linea[len(linea) - 1]
                num = ','.join(numero)
                posiciones = Busqueda(numero, buscado)
                if not Vacio(posiciones):
                    pos = ','.join(map(str, posiciones))
                    print(nombre + ": = " + num + " EL NUMERO " + buscado + " SE ENCUENTRA EN LA POSICION = " + pos,end="\n")
                else:
                    print(nombre + ": = " + num + " EL NUMERO " + buscado + " NO SE HA ENCONTRADO ", end="\n")
def Buscar(vec):
    for e in vec:
        if e == "BUSCAR":
            return True
    return False
def Ordenar(vec):
    for e in vec:
        if e == "ORDENAR":
            return True
    return False
def Imprimir(vec):
    for elemento in vec:
        print(elemento)
def Ascendente(vec):
    for i in range(len(vec)):
        for j in range(0, len(vec) - 1):
            if vec[j] > vec[j + 1]:
                temp = vec[j]
                vec[j] = vec[j + 1]
                vec[j + 1] = temp
    return vec
def Imprimirlo():
    print("*******Todas las listas******")
    for linea in cm:
        o = Ordenar(linea)
        b = Buscar(linea)
        numeros = QuitarComa(linea[1])
        nombre = linea[0]
        if o is True and b is False:
            print("---------SOLO ORDENAR---------")
            num = ','.join(Ascendente(numeros))
            print(nombre + ": ORDENADO = " + num, end="\n")
        elif o is False and b is True:
            print("---------SOLO BUSCAR---------")
            buscado = linea[len(linea) - 1]
            num = ','.join(numeros)
            posiciones = Busqueda(numeros, buscado)
            if not Vacio(posiciones):
                pos = ','.join(map(str, posiciones))
                print(nombre + ": = " + num + " EL NUMERO " + buscado + " SE ENCUENTRA EN LA POSICION = " + pos, end="\n")
            else:
                print(nombre + ": = " + num + " EL NUMERO " + buscado + " NO SE HA ENCONTRADO ", end="\n")
        elif o is True and b is True:
            print("-------ORDENAR Y BUSCAR-------")
            buscado = linea[len(linea) - 1]
            num = ','.join(Ascendente(numeros))
            posiciones = Busqueda(numeros, buscado)
            if not Vacio(posiciones):
                pos = ','.join(map(str, posiciones))
                print(nombre + ": ORDENADO = " + num + " EL NUMERO " + buscado + " SE ENCUENTRA EN LA POSICION = " + pos, end="\n")
            else:
                print(nombre + ": ORDENADO =" + num + " EL NUMERO " + buscado + " NO SE HA ENCONTRADO", end="\n")
        else:
            print("------NI BUSCAR NI ORDENAR------")
            num = ','.join(numeros)
            print(nombre + ": " + num, end="\n")
def HTML():
    lol = open('Archivo.html', 'w')
    inicio = """<html>
    <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <nav class="navbar navbar-dark bg-dark">
      <a class="navbar-brand">
        <img src="usacIcono.png" width="100" height="100">
      </a>
      <a class="navbar-brand">
      <h2><b> Práctica 1 - Lenguajes formales y de programación </b></h2>
      <h3><b> Allan Josué Rafael Morales - 201709196 </b></h3>
      </a>
    </nav>
    </head>
    <body>"""
    lol.write(inicio)
    datos = """
    <br>
    <br>
    \n"""
    lol.write(datos)
    lol.write("""
    <div class="container" style="text-align: center;"><h4 > <b> DATOS OPERADOS DEL ARCHIVO SELECCIONADO </b> <h4></div>
    <br>
    <div class="container" style="text-align: center;" > <ul class="list-group">""")
    for linea in cm:
        lol.write("<br>")
        o = Ordenar(linea)
        b = Buscar(linea)
        numero = QuitarComa(linea[1])
        nombreLista = linea[0]

        if o is True and b is False:
            print("ORDENADAS")
            num = ','.join(Ascendente(numero))
            lol.write("""<li class="list-group-item">""")
            lol.write(" LISTA: " + nombreLista + " ORDENADA = " + num + "\n")
            lol.write("</li>")
        elif o is False and b is True:
            print("BUSQUEDAS")
            buscado = linea[len(linea) - 1]
            num = ','.join(numero)
            posiciones = Busqueda(numero, buscado)
            if not Vacio(posiciones):
                pos = ','.join(map(str, posiciones))
                lol.write("""<li class="list-group-item">""")
                lol.write(" LISTA: " + nombreLista + " = " + num + " EL NUMERO " + buscado + " SE ENCUENTRA EN LA POSICION = " + pos + "\n")
                lol.write("</li>")
            else:
                lol.write("""<li class="list-group-item">""")
                lol.write(" LISTA: " + nombreLista + " = " + num + " EL NUMERO " + buscado + " NO SE HA ENCONTRADO " + "\n")
                lol.write("</li>")
        elif o is True and b is True:
            print("ORDENAR Y BUSCAR")
            buscado = linea[len(linea) - 1]
            num = ','.join(Ascendente(numero))
            posiciones = Busqueda(numero, buscado)
            if not Vacio(posiciones):
                pos = ','.join(map(str, posiciones))
                lol.write("""<li class="list-group-item">""")
                lol.write(" LISTA: " + nombreLista + " ORDENADA = " + num + " EL NUMERO " + buscado + " SE ENCUENTRA EN LA POSICION = " + pos + "\n")
                lol.write("</li>")
            else:
                lol.write("""<li class="list-group-item">""")
                lol.write(" LISTA: " + nombreLista + " ORDENADA = " + num + " EL NUMERO " + buscado + " NO SE HA ENCONTRADO " + "\n")
                lol.write("</li>")
        else:
            print("NI BUSCAR NI ORDENAR")
            num = ','.join(numero)
            lol.write("""<li class="list-group-item">""")
            lol.write(nombreLista + ": " + num + "\n")
            lol.write("</li>")
    lol.write('\n</ul> </div> \n')
    fin = """</body>
        </html>"""
    lol.write(fin)
    lol.close()

if __name__ == '__main__':
    Opcion = None
    while Opcion != 6:
        print('-------------------------------')
        print('********PRACTICA N.1********')
        print('1. Cargar archivos de entrada.')
        print('2. Desplegar listas ordenadas.')
        print('3. Desplegar búsquedas.')
        print('4. Desplegar todas.')
        print('5. Desplegar todas a archivo.')
        print('6. Salir.')
        print('-------------------------------')
        Opcion = int(input())
        if Opcion == 1:
            print("-------------------------------")
            print("Cargar Archivo:")
            root = abrirDoc()
            leerDoc(root)
            print(root)
            print()
            Imprimir(cm)
            cm = QuitarLineas(cm)
        elif Opcion == 2:
            print("-------------------------------")
            Ordenados()
        elif Opcion == 3:
            print("-------------------------------")
            Buscados()
        elif Opcion == 4:
            print("-------------------------------")
            Imprimirlo()
        elif Opcion == 5:
            print("-------------------------------")
            HTML()
        elif Opcion == 6:
            print("----------FINALIZADO-----------")
        else:
            print("Escoga una opcion valida")
