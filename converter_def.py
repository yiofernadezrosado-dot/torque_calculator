# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:01:59 2026

@author: Yidier
"""
def CeltoFah(C):
    F=(9.0/5.0)*C+32
    return F
def FahtoCel(F):
    return(5/9)*(F-32)
def RantoFah(R):
    return R-459.67
def FahtoRan(F):
    return F+459.67
def CeltoKel(C):
    return C+273.15
def KeltoCel(K):
    return K-273.16
def RantoCel(R):
    F=RantoFah(R)
    return FahtoCel(F)
def KeltoFah(K):
    C=KeltoCel(K)
    return CeltoFah(C)
def FahtoKel(F):
    C=FahtoCel(F)
    return CeltoKel(C)
def RantoKel(R):
    C=RantoCel(R)
    return CeltoKel(C)
def CeltoRan(C):
    F=CeltoFah(C)
    return FahtoRan(F)
def KeltoRan(K):    
    F=KeltoFah(K)
    return FahtoRan(F)
def CeltoNew(C):
    return C * (33.0 / 100.0)
def NewtoCel(N):
    return N * (100.0 / 33.0)
def FahtoNew(F):
    C = FahtoCel(F)
    return CeltoNew(C)
def NewtoFah(N):
    C = NewtoCel(N)
    return CeltoFah(C)