# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:26:26 2021

@author: DELL
"""
#Cek nilai huruf
ulang="y"
while ulang=="y" or ulang("Y"):
    print ("=========================")
    print ("       Nilai huruf       ")
    print ("=========================")

    n=0
    while int(n)>=0 and int(n)<=100:
        n=input ("--> Masukkan nilai anda:")
        if int(n)>=0 and int(n)<=100:
            if int(n)>=91: sts="A"
            elif int(n)>=81: sts="B"
            elif int(n)>=71: sts="C"
            else: sts="D"
            print("--> Status nilai anda:",sts)
            
            ulang = input("--> Ulang program? Y/T:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Nilai inputan 0-100)"
            print(pesan)
            break
        