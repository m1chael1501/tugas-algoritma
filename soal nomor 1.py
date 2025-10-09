total = int(input("masukkan total pengulangan(i): "))

jumlah = 0
terbesar = None
terkecil = None

for i in range (1,total +1):
    angka = int(input(f"Masukkan nilai ke-(i): "))
    jumlah += angka 
    
    if (terbesar is None) or (angka > terbesar):
        terbesar = angka
        
    if (terkecil is None) or (angka < terkecil):
        terkecil = angka

rata_rata = jumlah / total
print(f"nilai rata rata adalah:{rata_rata}")
print (f"nilai terbesar adalah:{terbesar}")
print (f"nilai terkecil adalah: {terkecil}")