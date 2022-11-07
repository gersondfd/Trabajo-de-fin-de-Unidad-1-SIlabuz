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
def seleccionar_menu(a):
    if a==1:
        leer_archivo()
    elif a==2:
        listar_libros()
    elif a==3:
        agregar_libro()
    elif a==4:
        eliminar_libro()
    elif a==5:
        buscar_isbn_titulo()
    elif a==6:
        ordenar_titulo()
    elif a==7:
        buscar_autor_editorial_genero()
    elif a==8:
        buscar_autores()    
    elif a==9:
        editar_libro()
    elif a==10:
        guardar_libros()
    else:
        print("No disponible")        
def normalizar_lista():
    j=len(misLibros[0])-4
    for i in range(1,(len(misLibros))):       
        while len(misLibros[0])<len(misLibros[i]):
            misLibros[0].append(str('Autor('+str(j)+') '))
            j+=1
def leer_archivo():
    with open('libros.csv', encoding="utf-8") as f:


    #    writer=csv.writer(f)
    #    writer.writerows(myData)

        reader=csv.reader(f)
        next(reader)
        for i in reader:
            #print(i)
            misLibros.append(i)
        print('\nSe cargaron '+str(len(misLibros)-1)+' libros.\n')
    normalizar_lista()
    seleccionar_menu(evaluar_menu(mostrar_menu()))
def listar_libros():
    #normalizar_lista()
    a=1
    for i in misLibros:
        if a>(len(misLibros))-1:
            break
        else:
            #print(misLibros[a])
            c=0
            for b in misLibros[a]:
                print(misLibros[0][c],":",b)
                c+=1
            a+=1
            print("")
    seleccionar_menu(evaluar_menu(mostrar_menu()))
def agregar_libro():
    m=[]
    print()
    for i in range(0,6):
        l=input("Ingrese "+misLibros[0][i]+": ")
        m.append(l)
    while True:
        a=input('¿Desea agregar más autores? (y/n) : ')
        if a=='y':
            b=input('Ingrese Autor('+str(len(m)-4)+') : ')
            m.append(b)
            continue
        elif a=='n':
            break
        else:
            print("Error. Ingrese sólo las letras (y) o (n).")
            continue
    misLibros.append(m)
    print('\nSe agregó 1 libro.\n')
    normalizar_lista()
    seleccionar_menu(evaluar_menu(mostrar_menu()))
def editar_libro():
    print("Editar un libro:\n")
    for i in range(1,len(misLibros)):
        print(str(i)+": "+(misLibros[i][1]))
    enl=int(input("\nIngrese un numero de la lista: "))
    for i in range(0,6):
        l=input("Ingrese nuevo "+misLibros[0][i]+": ")
        misLibros[enl][i]=l
    print()
    listar_libros()
    seleccionar_menu(evaluar_menu(mostrar_menu()))
def buscar_autores():
    nda=input("\nFiltrado de libros por número de autores.\n\nIngrese el número de autores: ")
    r8=0
    for i in range(1,len(misLibros)):
        if len(misLibros[i])==int(nda)+5:
            print()
            for j in range(0,len(misLibros[i])):
                print(misLibros[0][j],':',misLibros[i][j])
                r8+=1
            print()
    if r8==0:
        print("\nNo hay libro con tal cantidad de autores.\n")
    seleccionar_menu(evaluar_menu(mostrar_menu()))
def guardar_libros():
    with open('libros.csv','w', encoding="utf-8",newline='') as f:
        writer=csv.writer(f)
        for i in range(0,(len(misLibros)),1):
            writer.writerow(misLibros[i])
    seleccionar_menu(evaluar_menu(mostrar_menu()))
seleccionar_menu(evaluar_menu(mostrar_menu()))