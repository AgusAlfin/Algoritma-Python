# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 08:24:03 2021

@author: DELL
"""

def rp(uang):
            x = str(uang)
            if len(x) <= 3:
                return 'Rp. ' + x
            else:
                a = x[:-3]
                b = x[-3:]
                return rp(a) + '.' + b
            
ulang='y'
while ulang=='y' or ulang =='Y':
    
    lagi='y'
    while lagi == 'y' or lagi =='Y':
    #Menu makanan
        print("")
        print("========================================")
        print(" DAFTAR MENU MAKANAN ")
        print("========================================")
        print(" a = Nasi Goreng        -Rp 15.000")
        print(" b = Lontong Goreng     -Rp 14.900")
        print(" c = Bakso Goreng       -Rp 12.900")
        print(" d = Rujak Goreng       -Rp 13.000")
        print(" e = Rujak Bakso        -Rp 15.000")
        print(" f = Rujak Bakso Pecel  -Rp 17.000")
        print("----------------------------------------")
        
        #1. SIAPKAN VARIABEL
        kode =['a','b','c','d','e','f']
        namaBarang = ['Nasi Goreng','Lontong Goreng','Bakso Goreng',\
                      'Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
        harga1 = [15000, 14900, 12900, 13000, 15000, 17000]
        
        
        #2. INPUT PILIHAN
        pilihan = input(">> Masukkan Kode Makanan    = ")
        
        #3. INPUT QTY
        qty     = input(">> Masukkan Jumlah Makanan  = ")
        
        #4. HITUNG BAYAR
        ##cek nama barang dan ambil harga satuan
        i = 0
        while i<len(namaBarang):
            #jika value pada list kode[i] == pilihan
            if kode[i] == pilihan:
                #ambil nama barang
                nm_brg = namaBarang[i]
        
                #ambil harga satuan
                hrgsat = harga1[i]
                
            #jika tidak cocok, lanjut ke i berikutnya
            i+=1
        tot_byr = hrgsat * int(qty)
        lagi = input('Tambah Makanan Lagi? Y/T: ')
        if lagi == 't' or lagi =='T':
            
            
            #Menu minuman
            lagi2 = 'y'
            while lagi2 == 'y' or lagi2 =='Y':
                print("")
                print("========================================")
                print(" DAFTAR MENU MAINUMAN ")
                print("========================================")
                print(" a = Teh Panas/Hangat/Es  -Rp 2.500")
                print(" b = Kopi Dingin          -Rp 5.000")
                print(" c = Kopi Teh Panas       -Rp 6.500")
                print(" d = Cocacola Dingin      -Rp 3.500")
                print(" e = Cocacola Panas       -Rp 5.000")
                print("----------------------------------------")
                
                kode2 = ['a','b','c','d','e']
                minuman = ['Teh Panas/Hangat/Es','Kopi Dingin','Kopi Teh Panas',\
                           'Cocacola Dingin','Cocacola Panas']
                harga2 = [2500, 5000, 6500, 3500, 5000]
                
                pilihan2 = input('Masukkan kode minuman : ')
                qty2 = input('Masukkan jumlah minuman   : ')
                
                n=0
                while n<len(minuman):
                    if kode2[n] == pilihan2:
                        barang = minuman[n]
                        hrgsat2 = harga2[n]
                    n+=1
                totBayar2 = hrgsat2 * int(qty2)
                
                lagi2 = input('Tambah Minuman Lagi? Y/T: ')
                print()
                if lagi2 == 't' or lagi2 == 'T':     
                    
                    #Pembayaran
                    totalBayar = tot_byr + totBayar2
                    print('Total Harga   =', rp (totalBayar))
                    uangTunai = input('Uang Tunai    = ')
                    kembalian = int(uangTunai)-totalBayar
                
                    #5. TAMPILKAN 
                    print()
                    print('=============================================')
                    print('==============  STRUK BELI   ================')
                    print('=============================================')
                    print(">>> NAMA BARANG   : ",qty, nm_brg,'(',rp(hrgsat),')')
                    print('                     -->',rp(tot_byr))
                    print('                    ',qty2, barang,'(',rp(hrgsat2),')')
                    print('                     -->',rp(totBayar2))
                    print(("-------------------------------"))
                    print(">>> TOTAL BAYAR   : ", rp (totalBayar))
                    print('>>> UANG          : ', rp (uangTunai))
                    print('>>> KEMBALIAN     : ', rp (kembalian))
                    ulang=input('Ulangi Transaksi?Y/T: ')
                    print()
                    if ulang=='t' or ulang=='T':
                     break

"""
1. buatlah agar format uang tersebut memiliki digit ribuan
2. tambahkan fitur Mengulang transaksi
3. Challenge:
    - output ke Notepad
"""

"""
pada materi selanjutnya: 
    program akan dibuat agar pembeli dapat membeli 
    beberapa barang sekaligus dalam SATU kali transaksi
    clue: looping pada tambah Item.
"""