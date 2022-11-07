import csv
import os




def imprimir_libro(listadelibros,libro):
    for i in range(0,len(listadelibros[libro])):
        print(listadelibros[0][i],':',listadelibros[libro][i])
