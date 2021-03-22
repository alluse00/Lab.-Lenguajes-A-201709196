from AFDM import *
from AFDP import *
from Process import *
from HTML import *
from tkinter import *
from tkinter.filedialog import askopenfilename

REST = None
FACT = None
TKM = []
TKP = []
EM = []
EP = []

def TA():
    ruta = Tk()
    a = askopenfilename()
    ruta.withdraw()
    return a

def datosM():
    print('--------------------------------------')
    print('* * * * * Proyecto 1 - LFP * * * * * *')
    print('Ingenieria en Ciencias y Sistemas')
    print('Lenguajes formales y de programación')
    print('Sección A+')
    print('Estudiante: Allan Josué Rafael Morales')
    print('Carné: 201709196')
    print('--------------------------------------')
def menu():
    try:
        op = None
        while op != 6:
            print(' * * * * Menú Proyecto No.1 * * * * * ')
            print("1) Cargar menú.")
            print("2) Cargar orden.")
            print("3) Generar menú.")
            print("4) Generar factura.")
            print("5) No hace nada:(")
            print("6) Salir.")
            print('--------------------------------------')
            print('>>INGRESE UNA OPCIÓN:')
            op = int(input())
            if op == 1:
                ruta = TA()
                menu = afdM(ruta)
                TKM = menu[0]
                EM = menu[1]
                REST = OrdenarM(TKM)
                print('--------------------------------------')
            elif op == 2:
                ruta = TA()
                pedidos = afdP(ruta)
                TKP = pedidos[0]
                EP = pedidos[1]
                print('--------------------------------------')
            elif op == 3:
                if len(TKM) == 0:
                    print("Primero selecciones un archivo de menú")
                else:
                    if len(EM) == 0:
                        MHTML(REST, None)
                    else:
                        print("Existen errores en el menú")
                        TEHTML(EM)
                print('--------------------------------------')
            elif op == 4:
                if len(TKM) == 0:
                    print("Primero selecciones un archivo de menú")
                else:
                    FACT = OrdenarP(TKP)
                    print("Imprimir Factura: ")
                    FACT = processf(REST, FACT)
                    FACT.imprimir()
                    if (len(EP) == 0) or (FACT.facturaCorrecta is True):
                        FHTML(FACT, REST)
                    else:
                        print("Existen errores en el menú")
                        TEHTML(EP)
                print('--------------------------------------')
            elif op == 5:
                print("Te lo dije:(")
                print('--------------------------------------')
            elif op == 6:
                print(" Finalizado ")
                print('--------------------------------------')
            else:
                print("Escoja una opción valida")
    except ValueError:
        print("Ha ocurrido un error")

if __name__ == '__main__':
    datosM()
    menu()


