from tkinter import *
from tkinter.filedialog import askopenfilename

cm = []

def abrirDoc():
    root = Tk()
    name = askopenfilename()
    root.withdraw()
    return name

if __name__ == '__main__':
    Opcion = None
    while Opcion != 6:
        print('********PRACTICA N.1********')
        print('1. Cargar archivos.')
        print('2. Desplegar listas ordenadas.')
        print('3. desplegar busquedas.')
        print('4. Desplegar todas.')
        print('5. Desplegar todas a archivo.')
        print('6. Salir.')
        Opcion = int(input())
        if Opcion == 1:
            print("----------------------------------")
            print("Cargar Archivo")
            ruta = escoger_archivo()
            leer_archivo(ruta)
            print()
            print(ruta)
            print()
            imprimir(comando)
            print("----------------------------------")
            comando = separar_lineas(comando)
            imprimir(comando)
            print("----------------------------------")
        elif Opcion == 2:
            print("----------------------------------")
            imprimirOrdenadas()
            print("----------------------------------")
        elif Opcion == 3:
            print("----------------------------------")
            imprimirBusquedas()
            print("----------------------------------")
        elif Opcion == 4:
            print("----------------------------------")
            imptimir_todo()
            print("----------------------------------")
        elif Opcion == 5:
            print("----------------------------------")
            desplegarHTML()
            print("----------------------------------")
        elif int(Opcion) == 6:
            print("-----FINALIZADO-----")
