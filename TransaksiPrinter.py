# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:45:55 2021

@author: DELL
"""

#Transaksi printer
ulang="y"
while ulang=="y" or ulang=="Y":
    print("===========================")
    print(" Hitung Transaksi Printer ")
    print("===========================")
    
    harga=660000
    jml=0
    while jml>=0:
        jml=int(input ("--> Jumlah printer yang dibeli:"))
        if jml>=0:
            total = harga*jml
            print("--> Total pembayaran: Rp.", total)
    
            ulang = input("--> Ulang program? Y/T:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Nilai inputan harus lebih dari 0)"
            print(pesan)
            break