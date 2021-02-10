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
    print("****Listas Ordenadas****")
    for linea in cm:
        for elemento in linea:
            if elemento == "ORDENAR":
                numero = QuitarComa(linea[1])
                nombreLinea = linea[0]
                num = ','.join(sorted(numero))
                print(nombreLinea + ": ORDENADOS = " + num, end="\n")
def Buscados():
    print("****Listas Buscadas***")
    for linea in cm:
        for elemento in linea:
            if elemento == "BUSCAR":
                numero = QuitarComa(linea[1])
                buscado = linea[len(linea) - 1]
                nombre = linea[0]
                num = ','.join(numero)
                posiciones = Busqueda(numero, buscado)
                if not Vacio(posiciones):
                    pos = ','.join(map(str, posiciones))
                    print(nombre + " = " + num + " EL NUMERO " + buscado + " SE ENCUENTRA EN LA POSICION = " + pos, end="\n")
                else:
                    print(nombre + " = " + num + " EL NUMERO " + buscado + " NO SE HA ENCONTRADO ", end="\n")
def imprimir(vec):
    for elemento in vec:
        print(elemento)

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
            imprimir(cm)
            cm = QuitarLineas(cm)
        elif Opcion == 2:
            print("-------------------------------")
            Ordenados()
        elif Opcion == 3:
            print("-------------------------------")
            Buscados()
        elif Opcion == 4:
            print("-------------------------------")
            imptimir_todo()
            print("-------------------------------")
        elif Opcion == 5:
            print("-------------------------------")
            desplegarHTML()
            print("-------------------------------")
        elif Opcion == 6:
            print("-----FINALIZADO-----")
        else:
            print("Escoga una opcion valida")
