from typing import Set
import numpy as np
from numpy.lib.arraysetops import unique
import os 


def ContarColumnas(NombreArchivo):
   f=open(NombreArchivo+".csv",'r',encoding='ANSI')   
   line=f.readline().split(";") 
   Nrocolumnas= len(line)            
   f.close() 
   return Nrocolumnas

def ContarFilas(NombreArchivo):
    f=open(NombreArchivo+".csv",'r',encoding='ANSI') 
    line=f.readlines()
    Filas=len(line)
    f.close()
    return Filas-1

def LlenarMatriz(NombreArchivo):

    f=open(NombreArchivo+".csv",'r',encoding='ANSI')
    lines=f.readlines()    
    lista=[]
    Columnas=lines[0].split(";")
    lista.append(Columnas)
    for linea in unique(lines):
        l=linea.split(";")
        lista.append(l)        
    f.close()
    return lista

def EscribirArchivo(NombreArchivoFinal,matriz,NombreArchivoFuente):
    f = open(NombreArchivoFinal+".csv",'w',encoding='ANSI')    
    contador=0    
    for linea in matriz:        
        f.write(FormatearTexto(linea))        
        contador=contador+1
    f.close()

def FormatearTexto(linea):
    contador=0
    texto=""
    for l in linea:
        if(contador<len(linea)-1):            
            texto=texto+l+";"
            contador=contador+1
        else:
            texto=texto+l
    return texto


class Main():   
   RutaDeArchivoEntrada=input("Ingresar ubicacion donde esta alojado el archivo a modificar: \n")
   if(os.path.exists(RutaDeArchivoEntrada+".csv")==True):        
        print("Por favor espere... ")        
        Matriz=LlenarMatriz(RutaDeArchivoEntrada)
        Filas=ContarFilas(RutaDeArchivoEntrada)
        print("----Los registros a modificar son un total de: "+str(Filas)+"----")
        RutaDeArchivoSalida=input ("Ingresar el nombre del NUEVO archivo? \n")
        print("Por favor espere... ")
        EscribirArchivo(RutaDeArchivoSalida,Matriz,RutaDeArchivoEntrada)
            
   

   
