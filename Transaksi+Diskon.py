# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:21:42 2021

@author: DELL
"""

#Transaksi printer dengan diskon 15% jika total > 1,5jt
ulang="y"
while ulang=="y" or ulang=="Y":
    print("===========================")
    print(" Hitung Transaksi Printer ")
    print("===========================")
    
    harga=660000
    diskon= 15/100
    jml=0
    while jml>=0:
        jml=int(input ("--> Jumlah printer yang dibeli:"))
        if jml>=0:
            total = harga*jml
    
            if total>1500000:
                totDiskon = total*diskon
                totBayar = total-totDiskon
                print("--> Total diskon    : Rp.",int(totDiskon))
                print("--> Total pembayaran: Rp.",int(totBayar))
            else:
                totDiskon = 0
                print("--> Total diskon    : Rp.",int(totDiskon))
                print("--> Total pembayaran: Rp.",int(total))
    
            ulang = input("--> Ulang program? Y/T:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Nilai inputan harus lebih dari 0)"
            print(pesan)
            break
        