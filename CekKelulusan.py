# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 08:20:28 2021

@author: DELL
"""

#Cek kelulusan, jika nilai > 80 maka lulus
ulang = "y"
while ulang=="y" or ulang=="Y":
    
    print("=============================")
    print("        Cek Kelulusan        ")
    print("=============================")
    
    n=0
    while n<=100:
        n = int(input("--> Masukkan nilai :"))
        if int(n<=100):
            if int(n)>60:
                sts = "Lulus"
            else:
                sts = "Tidak Lulus"
            print ("--> Status anda:",sts)
    
            ulang = input("Ulangi program? Y/T:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Nilai inputan harus kurang dari 100)"
            print(pesan)
            break