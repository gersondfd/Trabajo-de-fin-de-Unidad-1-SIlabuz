import csv
import os
misLibros=[['ID       ','Título   ','Género   ','ISBN     ','Editorial','Autor(1) ']]
os.system("cls")

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