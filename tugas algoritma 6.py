berat =float(input("masukkan berat badanmu (kg): ")) 
tinggi=float(input("masukan tinggi badanmu (m): "))

bmi= berat/ (tinggi**2)

print("BMI kamu adalah:", round(bmi, 2))

if bmi < 18.5:
    print("kategori:kurus")
elif 18.5 <= bmi < 25:
    print("kategori:normal")
elif 25 <= bmi < 30:
    print("kategori:kelebihan berat badan")
else:
    print("kategori:obesitas")