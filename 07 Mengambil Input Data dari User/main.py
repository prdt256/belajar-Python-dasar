#====================================
#Belajar Python Dasar - Episode 7
#====================================

print("=== 1. INPUT STRING (BAWAAN) ===")
# Secara default, apa pun yang kamu ketik akan dianggap TEXT (String)
data_string = input("Masukkan nama kamu: ")
print("Halo", data_string, "!, tipe datanya:", type(data_string))


print("\n=== 2. JEBAKAN INPUT ANGKA ===")
# Kalau kita input angka tanpa dicasting, dia TETAP dianggap String
angka_salah = input("Masukkan angka pertama: ")
angka_kedua = input("Masukkan angka kedua  : ")
# Hasilnya bukan ditambah, tapi ditempel (karena string)
hasil_salah = angka_salah + angka_kedua
print("Hasil salah (String ditambahkan):", hasil_salah)


print("\n=== 3. SOLUSI: INPUT ANGKA DENGAN CASTING ===")
# Biar bisa dihitung secara matematika, kita bungkus dengan int() atau float()
angka_int   = int(input("Masukkan angka bulat: "))
angka_float = float(input("Masukkan angka desimal: "))

print("Angka bulat   :", angka_int, "-> tipe:", type(angka_int))
print("Angka desimal :", angka_float, "-> tipe:", type(angka_float))


print("\n=== 4. INPUT BOOLEAN ===")
# Khusus boolean, kita harus casting ke int dulu baru ke bool le!
# Karena kalau langsung bool(input()), ngetik "False" pun bakal tetap dianggap True 
# (Sebab string "False" itu ada isinya, tidak kosong)
data_bool = bool(int(input("Masukkan nilai boolean (0 untuk False, 1 untuk True): ")))
print("Data boolean :", data_bool, "-> tipe:", type(data_bool))