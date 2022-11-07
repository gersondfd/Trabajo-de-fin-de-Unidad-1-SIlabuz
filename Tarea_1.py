import csv
import os
misLibros=[['ID       ','Título   ','Género   ','ISBN     ','Editorial','Autor(1) ']]
os.system("cls")
def mostrar_menu():
    return input('\n\nBienvenido al Registro de Libros\n\nMenú de Operaciones\n\n1: Leer archivo de disco duro.\n2: Listar libros.\n3: Agregar libro.\n4: Eliminar libro.\n5: Buscar libro por ISBN o por título.\n6: Ordenar libros por título.\n7: Buscar libros por autor, editorial o género.\n8: Buscar libros por número de autores.\n9: Editar o actualizar datos de un libro.\n10: Guardar libros en archivo de disco duro.\n\nIngrese el numero de su operación: ')
def imprimir_libro(listadelibros,libro):
    for i in range(0,len(listadelibros[libro])):
        print(listadelibros[0][i],':',listadelibros[libro][i])
def evaluar_menu(a):
    try:
        b=int(a)
        if 0<=b and b<=10:
            return b
        else:
            print("\nError. Por favor, ingrese un numero de la lista.\n")
            evaluar_menu(mostrar_menu())
    except ValueError:
        print("\nError. Por favor, ingrese un numero de la lista.\n")
        evaluar_menu(mostrar_menu())