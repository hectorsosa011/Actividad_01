# -*- coding: utf-8 -*-
"""
Spyder Editor

Actividad_01 

"""
#----------------------------------------------------------------------------
import os
import math
import statistics

cwd = os.getcwd()

as_files = []

"Busqueda de archivos que terminen en .AS dentro de la carpeta de trabajo"
#os.system('teqc -O.dec 30 +obs ' + name +' CRNO20201201_000000.AS')

def asfiles(cwd):
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(".AS"):
                as_files.append(file)
                #print(file)
                
asfiles(cwd)
#print(as_files)
#----------------------------------------------------------------------------
"Ejecución de teqc para los archivos.AS y creacion de archivos.o,"
#def o_files(as_files):
#    for file in as_files:         
#        name_ofile = file.split('_')[0]+'.o'
#        print(name_ofile)
#        os.system('teqc -O.dec 30 +obs ' + name_ofile +' '+ file)
#o_files(as_files)  

#----------------------------------------------------------------------------
"---- listas de prueba"
Xcoord = []
Ycoord = []
Zcoord = []    
"Lectura de la linea 10 de los archivos.o y el agregarlos a una lista"
def xyz_coord(cwd):
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(".o"):
                #print(file)
                with open(file) as f:            
                    lines= f.readlines()[9:10]
                    for line in lines:
                        #print(line)
                        Xcoord.append((line.strip().split(" "))[0])
                        Ycoord.append((line.strip().split(" "))[1])
                        Zcoord.append((line.strip().split(" "))[3]) 
                #print(file)

xyz_coord(cwd)

#------------- PRUEBA INDIVIDUAL ---------------------- 
#with open('CRNO20201201.o') as f:
#    lines= f.readlines()[9:10]
#    for line in lines:        
#        Xcoord.append((line.strip().split(" "))[0])
#        Ycoord.append((line.strip().split(" "))[1])
#        Zcoord.append((line.strip().split(" "))[3])    
#        #print(strip_line)
#print("listas x y z")
#print(Xcoord)
#print(Ycoord)
#print(Zcoord)

#----------------------------------------------------------------------------
"Convetir lista cadena Xcoord a numeros float"
X_list= list(map(float, Xcoord))
#print(X_list)

"Convetir lista cadena Ycoord a numeros float"
Y_list= list(map(float, Ycoord))
#print(Y_list)

"Convetir lista cadena Zcoord a numeros float"
Z_list= list(map(float, Zcoord))
#print(Z_list)

#----------------------------------------------------------------------------
"Media de las coordenadas geocentricas"
print ("Coordenadas geocentricas")
Xmean = statistics.mean(X_list) 
print("  X =", Xmean) 
Ymean = statistics.mean(Y_list) 
print("  Y =", Ymean) 
Zmean = statistics.mean(Z_list)
print("  Z =", Zmean)

#----------------------------------------------------------------------------
" Transformación entre coord geocéntricas (X, Y, Z) a geodésicas (λ,φ,h) "
a = 6378137
b = 6356752.314

#"---- Resultados, comprobacion de e, e_prim y P. -------"
e = ((a**2 - b**2)/(a**2))
#print(" e: ", e)

e_prim = ((a**2 - b**2)/(b**2))
#print(" e_prim: ",e_prim)

p = math.sqrt((Xmean)**2 + (Ymean)**2)
#print(" p: ",p)

print("-----------------")
print ("Coordenadas geodesicas")

"----- Formulas -------"
thetaR = math.atan((Zmean * a )/(p * b))

#"---- Variables de Sin y Cos para theta    -------"
thetaRS = (math.sin(thetaR))**3
thetaRC = (math.cos(thetaR))**3

#"---- Formula para encontrar phi  -------"
phi = math.atan(((Zmean + e_prim * b * thetaRS )/(p - e * a * thetaRC)))
print("  φ =", math.degrees(phi)) # Resultado en grados

#"---- Formula para encontrar N   -------"
phiRC = (math.sin(phi))**2 # phi en radianes para Sin
N = ( a / math.sqrt( (1 - e * phiRC)))

#"---- Formula para encontrar landa   -------"
landa = math.degrees(math.atan(Ymean/Xmean))
print("  λ =",landa)

#"---- Formula para encontrar h   -------"
phiRC = math.cos(phi) #phi en radianes para Cos
h =  ( p / (phiRC))-N
print("  h =",h)
