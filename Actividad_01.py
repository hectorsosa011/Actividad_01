# -*- coding: utf-8 -*-
"""
Spyder Editor

Actividad_01 

"""

import os
import math
import statistics

cwd = os.getcwd()

as_files = []

Xcoord = []
Ycoord = []
Zcoord = []
#os.system('teqc -O.dec 30 +obs ' + name +' CRNO20201201_000000.AS')


def asfiles(cwd):
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(".AS"):
                as_files.append(file)
                print(file)
                
#asfiles(cwd)
#print(as_files)

#def o_files(as_files):
#    for file in as_files:         
#        name_ofile = file.split('_')[0]+'.o'
#        print(name_ofile)
#        os.system('teqc -O.dec 30 +obs ' + name_ofile +' '+ file)
#o_files(as_files)  

#for root, dirs, files in os.walk(cwd):

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

print(Xcoord)
print(Ycoord)
print(Zcoord)

#Xmean = statistics.mean(Xcoord)
#print (Xmean)


#print(Xcoordd)

#Xcoordd = ['408079.7292', '408078.8105', '408078.8839', '408078.5278', '408078.0667', '408078.7420', '408078.2101', '408080.3641', '408078.3534', '408078.2339', '408077.4825', '408077.8019', '408079.1196', '408080.2453', '408078.9651', '408077.4631', '408079.7197', '408076.9984', '408074.7555', '408074.6207', '408078.1237', '408079.4599', '408079.1861', '408080.6267', '408078.4762', '408077.6788', '408078.7968', '408078.5218', '408077.8401', '408077.3832', '408077.7307']

#res = [float(sub.split('.')) for sub in Xcoordd] 
  
# print result 
#print("The list after Extracting numbers : " + str(res))

new_l = list(map(float, Xcoord))

print(new_l)


x = statistics.mean(new_l) 
  
# Printing the mean 
#print("Mean is :", x) 

#lol