#====================================
#Belajar Python Dasar - Episode 4
#====================================

# 1. Variabel adalah tempat menyimpan data (Assignment)
# Menaruh nilai 10 ke dalam variabel bernama 'a'
a = 10
x = 5
panjang = 1000

# 2. Cara memanggil variabel
print("Nilai a =", a)
print("Nilai x =", x)
print("Nilai panjang =", panjang)

# 3. Penamaan variabel
nilai_y = 15 # menggunakan underscore itu bagus
juta10 = 10000000 # angka boleh di belakang, tapi...
# 10juta = 10000000 <- INI SALAH (tidak boleh diawali angka)
nilaiZ = 17.5 # menggunakan camelCase juga boleh

# 4. Mengubah nilai (Re-assignment)
# Variabel 'a' yang tadi isinya 10, kita ganti jadi 7
a = 7
print("Nilai a baru =", a)

# 5. Assignment indirect
# Memasukkan nilai variabel 'a' ke dalam variabel 'b'
b = a
print("Nilai b =", b)

#nilai variabel bisa diubah
nilai = 1
print("Nilai Sekarang adalah = ", nilai)

nilai = 2
print("Nilai yang diperbarui = ", nilai)