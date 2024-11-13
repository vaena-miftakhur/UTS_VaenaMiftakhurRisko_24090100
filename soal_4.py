berat_badan = float(input("Masukkan Berat Badan (Kg): "))
tinggi_badan = float(input("Masukkan Tinggi Badan (M): "))
bmi = berat_badan / (tinggi_badan ** 2)

print("\nBerat Badan : ", berat_badan, "Kg")
print("Tinggi Badan : ", tinggi_badan, "M")
print("Nilai BMI Anda : {:.2f}".format(bmi))

if bmi < 18.5:
    print("Kategori BMI : Berat Badan Kurang")
elif 18.5 <= bmi < 24.9:
    print("Kategori BMI : Berat Badan Normal")
elif 25 <= bmi < 29.9:
    print("Kategori BMI : Kelebihan Berat Badan")
else:
    print("Kategori BMI : Obesitas")

