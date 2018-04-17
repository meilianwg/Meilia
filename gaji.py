gaji = int(input("Masukkan Gaji:"))
berkeluarga = (False, True)[input("Sudah Berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True)[input("Punya Rumah? (Y/T)") == "Y"]

if gaji > 3000000:
    print ("Gaji Sudah Di Atas UMR")
    if berkeluarga:
        print("Wajib Ikut Asuransi Dan Menabung Untuk Pensiun")
    else:
        print("Tidak Perlu Ikut Asuransi")

    if punya_rumah:
        print("Wajib Bayar Pajak Rumah")
    else:
        print("Tidak Wajib Bayar Pajak Rumah")
else:
    print("Gaji Belum UMR")
        
