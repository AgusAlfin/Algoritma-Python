# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 08:18:29 2021

@author: DELL

Buat program untuk menghitung biaya total pengiriman barang di perusahaan Ekspedisi
Lorena di Malang
1. set variabel kota, jarak, ongkirperkm, totongkir
2. input pilihan kota
3. jika kota Sby, jarak = 169, ongkirperkm=2500, selain itu
jika kota Bdg, jarak = 452, ongkirperkm=4000
4. totongkir = jarak * ongkirperkm
5. tampilkan kota, totongkir
"""

ulang='y'
while ulang=='y' or ulang =='Y':
    print ("=============================================")
    print(" DAFTAR OLI UD. Matahari ")
    print("=============================================")
    print(" Kode = A. Duration SW20 1L")
    print("        B. Castrol Magnatec 1L")
    print('        C. Federal Supreme XX 1L')
    print('        D. Yamalube 1L')
    print('        E. Shell 1L')

    #jika menggunakan list Kode dibawah ini, maka metode yang digunakan
    #adalah mendeteksi indeks value yang terpilih pada list kode.
    #caranya: melakukan pencarian pada list kode menggunakan 
    # nilai kode yang diinputkan
    #salah satu metode : gunakan while
    #algoritma:
    # baca berulang2 index dalam list kode, jika value sama dengan 
    # value pilihan, ambil index nya

    kode =['a','b','c','d','e']
    merk = ['Duration SW20 1L','Castrol Magnatec 1L', 'Federal Supreme XX 1L',\
            'Yamalube 1L', 'Shell 1L']
    hrg = [53000,50000,54000,45000,46000]
    diskon = 5/100
    Ppn = 1/100

    pilihan = input("Masukkan Kode Pilihan = ")
    
    jumlah = int(input('Jumlah Pembelian      = '))
    
    #identifikasi pilihan
    idx=kode.index(pilihan)
    
    #cetak tampilan layar
    print("--> Merk Oli          = " + str(merk[idx]))
    print("--> Harga Satuan      = Rp." + str(hrg[idx]))
    
    #hitung transksi
    total = hrg[idx]*jumlah
    if total>=200000:
            totDiskon = total*diskon
    else:
            totDiskon = 0 
    
    totHarga2 = total-totDiskon
    totPpn = totHarga2*Ppn
    totHarga3 = totHarga2+totPpn
    
    #tampilkan total ongkir
    print("----------------------------------------------")
    print('--> Diskon            = Rp.', int(totDiskon))
    print('--> PPN               = Rp.', int(totPpn))
    print("--> Total Harga       = Rp.", int(totHarga3))
    ulang=input('Ulangi Transaksi?Y/T: ')
    print()
    if ulang=='t' or ulang=='T':
            break
    