#PROGRAM NILAI AKHIR MAHASISWA
#MEILIA NAWANG NINGRUM
321710282
print ()
print ()


nama =(input("Masukkan Nama : "))
uts = (input("Masukkan Nilai UTS : "))
uas = (input("Masukkan Nilai UAS : "))
tgs = (input("Masukkan Nilai Tugas : "))
print ("Nama        : %s"%nama)
print ("Nilai UAS   : %d %uas)
print ("Nilai UTS   : %d %uts)
print ("Nilai Tugas : %d %tgs)

nilai = ( uts + uas + tgs )/3
print ("Nilai Rata-Rata :  %d"%nilai)
print ("Nilai Huruf     : ")

if nilai >= 85 :
    print ("A")

elif nilai >= 75 :
    print ("B")

elif nilai >= 65 :
    print ("C")

elif nilai >= 55 :
    print ("D")


if nilai <= 55 :
    print ("Keterangan : TIDAK LULUS")
else :
    print ("Keterangan : LULUS")
