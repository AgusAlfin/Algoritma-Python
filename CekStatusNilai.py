# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 08:23:29 2021

@author: DELL
"""
#cek status nilai
ulang = "y"
while ulang=="y" or ulang=="Y":
    print ("=========================")
    print ("    CEK STATUS NILAI     ")
    print ("=========================")
    
    n=1
    while int(n)>=0 and int(n)<=100:
        n=input("--> Masukkan Nilai:")
        #cek batasan inputan usia 0-100
        if int(n)>=0 and int(n)<=100:
            if int(n)>80: sts="Baik Sekali"
            elif int(n)>=65: sts="Baik"
            elif int(n)>=55: sts="Cukup"
            elif int(n)>=40: sts="Kurang"
            else: sts="Kurang Sekali"
            print("--> Status nilai anda:",sts)
            
            ulang = input("--> Ulang program? Y/T:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Nilai inputan 0-100)"
            print(pesan)
            break