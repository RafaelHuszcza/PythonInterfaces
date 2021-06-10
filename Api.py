# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:02:18 2020

@author: Rafael
"""

import csv
import matplotlib.pyplot as pl
from numpy import polyfit, linspace, poly1d

def funcaoGrafico(fileName):
    AD = []
    VR = []    
    #abrir arquivo pela interface getOpenFileName()
    with open(fileName, 'r') as arq:
        tabela = csv.reader(arq, delimiter=";")
        for l in tabela:
            if l:                              
                AD.append(int(l[0]))
                VR.append(float(l[1]))
    mr = 0                                                                         #Menor residuo
    for x in range(1,6):
        p = polyfit(AD,VR,deg=x, full=True)              
        
        if mr == 0:
            mr = p[1]
            coeficientes = p[0]
        elif p[1] < mr:
            mr = p[1]
            coeficientes = p[0]          
               
    ADO = sorted(AD)
    VRO = sorted(VR)
    
    X = linspace(ADO[0],ADO[-1])
    Y = []
    
    ep = poly1d(coeficientes)         #apresentar equação polinomial
    
    for i in X:
       Y.append (ep(i)) 
    
    return ((ep),(ADO),(VRO),(X),(Y),(AD),(VR))

def LinhaBonita(p):
    txt = " <html><head/><body><body><p>y = "
    ordem = len(p.c) - 1
    
    for item in p.c:
        txt += "{:.4f}".format(item)
        if ordem:
            txt += "x" + ('<span style=" vertical-align:super;">'+str(ordem)+'</span>' if ordem > 1 else "") + " + "
        ordem -= 1
    txt +="</p></body></html>"
    return txt
    
    
    
    
