# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#cek golongan usia
ulang = "y"
while ulang=="y" or ulang=="Y":
    print ("=========================")
    print("     CEK GOLONGAN USIA    ")
    print ("=========================")
    
    n=1
    while int(n)>0 and int(n)<=100:
        n = input("--> Masukkan Usia: ")
        #cek batasan inputan usia 0-100
        if int(n)>0 and int(n)<=100:
            if int(n)>=60: sts="lansia"
            elif int(n)>=35: sts="dewasa"
            elif int(n)>=18: sts="pemuda"
            elif int(n)>=15: sts="remaja"
            else: sts="anak"
            print (sts)

            ulang = input("--> Ulang program? Y/T:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Masukkan angka usia 0-100 saja)"
            print(pesan)
            break